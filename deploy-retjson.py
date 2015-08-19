#! /usr/bin/python3
# encode:utf-8
import subprocess

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
        cmdAttach = ["/usr/bin/lxc-attach"] + lxcNameSet + ["--"]
        onSh = ["/bin/sh", "-c"] 

        lxcHome = lxcPath + lxcName + lxcRoot + homeDir 
        
        # cmd rm for test
        cmdRm = ["/bin/rm"] + ["-rf"]+ [lxcHome+dirname] 
        
        cmdMkdir = ["/bin/mkdir"] + [lxcHome+dirname] 
        
        cmdCp = ["/bin/cp"] + [filename] + [lxcHome+dirname] 

        cmdChown = ["/bin/chown " +username + ":" + username+ " " + homeDir+dirname+filename]

        socatExec = homeDir+dirname+filename
        attachSocat = ["/usr/bin/socat TCP4-LISTEN:8000,fork,reuseaddr EXEC:\""+socatExec+"\" &"]

        try:
            # subprocess.check_call(cmdRm)
            subprocess.check_call(cmdMkdir)
            subprocess.check_call(cmdCp)
            subprocess.check_call(cmdAttach + onSh + cmdChown)
            subprocess.check_call(cmdAttach + onSh + attachSocat)
                
        except subprocess.CalledProcessError as e:
            print('subprocess.CalledProcessError: cmd:%s returncode:%s' % (e.cmd, e.returncode))
            

if __name__ == '__main__':
    main()

