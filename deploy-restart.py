#! /usr/bin/python
# encode:utf-8
import argparse
import subprocess

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('pp', metavar='PP', help='print lines containing this pattern.')
    args = parser.parse_args()
    listname = args.pp
    
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

