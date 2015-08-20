#! /usr/bin/python3
# encode:utf-8
import subprocess
import shutil
import os

def main():
    lxcApList = ["ubuntu-ap1", "ubuntu-ap2"]
    lxcNginxList = ["ubuntu-nginx"]
    weightList = {lxcApList[0]:1, lxcApList[1]:3}
    
    username = "ubuntu"
    lxcPath = "/var/lib/lxc/"
    lxcRoot = "/rootfs"

    nginxConfPath = "/etc/nginx/sites-enabled/"
    confDefault = "default"
    confFilename = "conf-infoloc"
    appName = "nginx"
    upstreamName = "apserver"
    portNum = 8000
    
    # get Aps ip address    
    apIpAddr = {}
    cmdGetLxcInfo = ["/usr/bin/lxc-ls", "--fancy"]
    copInfo = subprocess.check_output(cmdGetLxcInfo).decode("utf-8")
    for info in copInfo.strip().split("\n")[2:]:
        infolist = info.strip().split()
        apIpAddr[infolist[0]] = infolist[2]
    
    # make upstream config
    upstreamConf = "upstream " + upstreamName +"{\n"
    for apName in lxcApList:
        upstreamConf += "server " + apIpAddr[apName] + ":" + str(portNum) + " weight=" + str(weightList[apName])+ ";\n"
    upstreamConf += "}\n"

    for lxcName in lxcNginxList:
        confPath = lxcPath + lxcName + lxcRoot + nginxConfPath
        lxcNameSet = ["-n", lxcName]
        cmdAttach = ["/usr/bin/lxc-attach"] + lxcNameSet + ["--"]

        # nginx install
        insNginx = ["./aptget-lxc.py", appName, lxcName]
        subprocess.check_call(insNginx)

        # stop nginx service 
        cmdStopService = ["/usr/sbin/service", appName, "stop"]
        subprocess.check_call(cmdAttach + cmdStopService)
        print(lxcName+":"+appName+" stop")
 
        # write configs
        shutil.copyfile(confPath+confDefault, "./"+confDefault+".old")
        os.remove(confPath+confDefault)
        shutil.copyfile(confFilename, confPath+confDefault)
        f = open(confPath+confDefault, "a")
        try:
            f.write(upstreamConf)
        except:
            print("!!!")
        finally:
            f.close()
        
        # start nginx service
        cmdStartService = ["/usr/sbin/service", appName, "start"]
        subprocess.check_call(cmdAttach + cmdStartService)        
        print(lxcName+":"+appName+" start")
        
if __name__ == '__main__':
    main()
