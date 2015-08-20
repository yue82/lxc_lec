#! /usr/bin/python3
# encode:utf-8
import subprocess

def main():
    lxcApList = ["ubuntu-ap1", "ubuntu-ap2"]
    lxcNginxList = ["ubuntu-nginx"]
    
    username = "ubuntu"
    lxcPath = "/var/lib/lxc/"
    lxcRoot = "/rootfs"

    service = "nginx"

    # get Aps ip address    
    apIpAddr = {}
    cmdGetLxcInfo = ["/usr/bin/lxc-ls", "--fancy"]
    copInfo = subprocess.check_output(cmdGetLxcInfo).decode("utf-8")
    for info in copInfo.strip().split("\n")[2:]:
        infolist = info.strip().split()
        apIpAddr[infolist[0]] = infolist[2]

    for lxcName in lxcNginxList:
        # nginx install
        insNginx = ["./aptget-lxc.py", "nginx", lxcName]
        subprocess.check_output(insNginx)

        # stop nginx service 
        cmdStopService = ["/bin/service", service, "stop"]

        # make location config

        # make upstream config

        # write configs

        # start nginx service
        cmdStartService = ["/bin/service", service, "start"]
        
        
if __name__ == '__main__':
    main()
