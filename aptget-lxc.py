#! /usr/bin/python
# encode:utf-8
import argparse
import subprocess
import sys

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('pp', metavar='PP', help='print lines containing this pattern.')
    parser.add_argument('qq', metavar='QQ', help='print lines containing this pattern.')
    args = parser.parse_args()
    insTool = args.pp
    listname = args.qq
    
    if listname == "all":
        lxcList=["ubuntu-ap1", "ubuntu-ap2", "ubuntu-nginx"]
    elif listname == "aps":
        lxcList=["ubuntu-ap1", "ubuntu-ap2"]
    elif listname == "nginx":
        lxcList=["ubuntu-nginx"]
    else:
        print "2nd arg is not 'all' or 'aps' or 'nginx'"
        print "set lxcname = " + listname
        lxcList = [listname]

    # deploy Socat
    for lxcName in lxcList:
        lxcNameSet = ["-n", lxcName]
        cmdAttach = ["/usr/bin/lxc-attach"] + lxcNameSet + ["--"]
        
        attachInstall = ["/usr/bin/apt-get", "install", "-y", insTool]
        
        subprocess.check_call(cmdAttach + attachInstall)
        print "#"*10 + "end on " + lxcName + "#"*10
            
if __name__ == '__main__':
    main()

