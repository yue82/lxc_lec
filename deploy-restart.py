#! /usr/bin/python3
# encode:utf-8
import subprocess
import sys

def main():
    lxcSocatList=["ubuntu-ap1", "ubuntu-ap2", "ubuntu-nginx"]

    # stop same name LXC
    for lxcName in lxcSocatList:
        lxcNameSet = ["-n", lxcName]
        cmdStop = ["/usr/bin/lxc-stop"] + lxcNameSet
        
        # failure ok
        subprocess.call(cmdStop)
    
    # Start lxc
    for lxcName in lxcSocatList:
        lxcNameSet = ["-n", lxcName]
        cmdStart = ["/usr/bin/lxc-start"] + lxcNameSet + ["-d"]

        try:
            subprocess.check_call(cmdStart)
            
        except subprocess.CalledProcessError as e:
            print('subprocess.CalledProcessError: cmd:%s returncode:%s' % (e.cmd, e.returncode))
        
if __name__ == '__main__':
    main()

