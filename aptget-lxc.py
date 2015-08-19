#! /usr/bin/python
# encode:utf-8
import argparse
import subprocess
import sys

def main():

    lxcList=["ubuntu-ap1", "ubuntu-ap2", "ubuntu-nginx"]
    
    parser = argparse.ArgumentParser()
    parser.add_argument('pp', metavar='PP', help='print lines containing this pattern.')
    args = parser.parse_args()
    insTool = args.pp

    try:
        # deploy Socat
        for lxcName in lxcList:
            lxcNameSet = ["-n", lxcName]
            cmdAttach = ["/usr/bin/lxc-attach"] + lxcNameSet + ["--"]
            
            attachInstall = ["/usr/bin/apt-get", "install", "-y", insTool]
          
            subprocess.check_call(cmdAttach + attachInstall)
            print "#"*10 + "end install on " + lxcName + "#"*10

    except subprocess.CallProcessError, (p):
        print 'subprocess.CalledProcessError: cmd:%s returncode:%s' % (p.cmd, p.returncode)
        sys.exit(1)
        
if __name__ == '__main__':
    main()

