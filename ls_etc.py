#! /usr/bin/python
# encode:utf-8
import subprocess
import sys
import pdb

argvs = sys.argv
if len(argvs) != 2:
  print "Please input 1 argument"
  quit()

searchWord = argvs[1]

cmd1 = "ls -a /etc/"
p1 = subprocess.Popen(cmd1.strip().split(" "), stdout=subprocess.PIPE)
stdout_data, stderr_data = p1.communicate()
p1.stdout.close()

if stderr_data != None:
  print "Error", stderr_data
  quit()
  
filelist = stdout_data.strip().split("\n")
for file in filelist:
  if file.find(searchWord) != -1:
    print file
