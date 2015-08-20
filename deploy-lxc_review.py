#! /usr/bin/python
# encode:utf-8
import argparse
import subprocess
import sys

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('pp', metavar='PP', help='print lines containing this pattern.')
    args = parser.parse_args()
    if args.pp == "go": goSocat = True
    else: goSocat = False

    lxcList=["ubuntu-nginx"]
    lxcSocatList=["ubuntu-ap1", "ubuntu-ap2"]
    
    # Destroy same name LXC
    for lxcName in lxcList+lxcSocatList:
        lxcNameSet = ["-n", lxcName]
        cmdStop = ["/usr/bin/lxc-stop"] + lxcNameSet
        cmdDestroy = ["/usr/bin/lxc-destroy"] + lxcNameSet
        
        # failure ok
        subprocess.call(cmdStop)
        subprocess.call(cmdDestroy)

    try:
        # Create and Start
        for lxcName in lxcList+lxcSocatList:
            lxcNameSet = ["-n", lxcName]
            cmdCreate = ["/usr/bin/lxc-create", "-t", "ubuntu"] + lxcNameSet
            cmdStart = ["/usr/bin/lxc-start"] + lxcNameSet + ["-d"]
          
            subprocess.check_call(cmdCreate)
            subprocess.check_call(cmdStart)

        # deploy Socat
        for lxcName in lxcSocatList:
            lxcNameSet = ["-n", lxcName]
            cmdAttach = ["/usr/bin/lxc-attach"] + lxcNameSet + ["--"]
            onSh = ["/bin/sh", "-c"] 
            
            attachInstallSocat = ["/usr/bin/apt-get", "install", "-y", "socat"]
            socatExec = "/bin/hostname"
            attachSocat = ["/usr/bin/socat TCP4-LISTEN:8000,fork,reuseaddr EXEC:\""+socatExec+"\" &"]
          
            subprocess.check_call(cmdAttach + attachInstallSocat)
            if goSocat:
                subprocess.check_call(cmdAttach + onSh + attachSocat)

    except subprocess.CalledProcessError, (p):
        print 'subprocess.CalledProcessError: cmd:%s returncode:%s' % (p.cmd, p.returncode)
        sys.exit(1)
        
if __name__ == '__main__':
    main()

