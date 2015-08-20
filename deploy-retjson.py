#! /usr/bin/python3
# encode:utf-8
import subprocess
import os
import shutil

def main():
    lxcList=["ubuntu-ap1", "ubuntu-ap2"]
    username = "ubuntu"
    lxcPath = "/var/lib/lxc/"
    lxcRoot = "/rootfs"
    homeDir = "/home/"+username+"/"
    dirname = "scripts/"
    filename = "ret_json.py"
    
    for lxcName in lxcList:
        lxcNameSet = ["-n", lxcName]
        lxcHome = lxcPath + lxcName + lxcRoot + homeDir 
        cmdAttach = ["/usr/bin/lxc-attach"] + lxcNameSet + ["--"]
        onSh = ["/bin/sh", "-c"] 
                
        cmdChownDir = ["/bin/chown " +username + ":" + username+ " " + homeDir + dirname]
        cmdChownFile = ["/bin/chown " +username + ":" + username+ " " + homeDir + dirname + filename]
        
        insSar = ["./aptget-lxc.py", "sysstat", lxcName]

        socatExecFile = homeDir+dirname+filename
        attachSocat = ["/usr/bin/socat TCP4-LISTEN:8000,fork,reuseaddr EXEC:\""+socatExecFile+"\" &"]
        
        # rm for test
        shutil.rmtree(lxcHome + dirname)        
        
        # ready to file
        os.mkdir(lxcHome + dirname)
        shutil.copyfile(filename, lxcHome + dirname + filename)
        subprocess.check_call(cmdAttach + onSh + cmdChownDir)
        subprocess.check_call(cmdAttach + onSh + cmdChownFile)
        os.chmod(lxcHome + dirname + filename, 755)
        # sar command install
        subprocess.check_call(insSar)
        # ready to TCP-LISTEN
        subprocess.check_call(cmdAttach + onSh + attachSocat)
        
if __name__ == '__main__':
    main()

