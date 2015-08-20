#! /usr/bin/python3
# encode:utf-8
import subprocess

def main():
    # lxcList=["ubuntu-ap1", "ubuntu-ap2", "ubuntu-nginx"]
    lxcList=["ubuntu-ap1", "ubuntu-ap2"]

    # stop same name LXC
    for lxcName in lxcList:
        lxcNameSet = ["-n", lxcName]
        cmdStop = ["/usr/bin/lxc-stop"] + lxcNameSet
        
        # ignore failure
        subprocess.call(cmdStop)
    
    # Start lxc
    for lxcName in lxcList:
        lxcNameSet = ["-n", lxcName]
        cmdStart = ["/usr/bin/lxc-start"] + lxcNameSet + ["-d"]

        subprocess.check_call(cmdStart)
        print("start " + lxcName)

if __name__ == '__main__':
    main()

