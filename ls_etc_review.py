#! /usr/bin/python
# encode:utf-8
import subprocess
import sys
import argparse
import pdb

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pp', metavar='PP', help='print lines containing this pattern.')
    args = parser.parse_args()
    searchWord = args.pp
    
    cmd1 = ["/bin/ls", "-a", "/etc/"]
    try:
        cop1 = subprocess.check_output(cmd1, stderr=subprocess.STDOUT)
    except subprocess.CallProcessError, (p):
        print 'subprocess.CalledProcessError: cmd:%s returncode:%s' % (p.cmd, p.returncode)
        sys.exit(1)
        
    filelist = cop1.strip().split("\n")
    for file in filelist:
        if file.find(searchWord) != -1:
            print file

if __name__ == '__main__':
  main()

