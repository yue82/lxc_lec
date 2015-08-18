#! /usr/bin/python
# encode:utf-8
import subprocess
import sys

def main():

  lxcList=["ubuntu-nginx"]
  lxcSocatList=["ubuntu-ap1", "ubuntu-ap2"]

  # Destroy same name LXC
  for lxcName in lxcList+lxcSocatList:
    lxcNameSet = ["-n", lxcName]
    cmdStop = ["lxc-stop"] + lxcNameSet
    cmdDestroy = ["lxc-destroy"] + lxcNameSet

    subprocess.call(cmdStop)
    subprocess.call(cmdDestroy)

  # Create and Start
  for lxcName in lxcList+lxcSocatList:
    lxcNameSet = ["-n", lxcName]
    cmdCreate = ["lxc-create", "-t", "ubuntu"] + lxcNameSet
    cmdStart = ["lxc-start"] + lxcNameSet + ["-d"]

    subprocess.call(cmdCreate)
    subprocess.call(cmdStart)

  # deploy Socat
  for lxcName in lxcSocatList:
    lxcNameSet = ["-n", lxcName]
    cmdAttach = ["lxc-attach"] + lxcNameSet + ["--"]
    onSh = ["sh", "-c"] 

    attachInstallSocat = ["apt-get", "install", "-y", "socat"]
    socatExec = "hostname"
    attachSocat = ["socat TCP4-LISTEN:8000,fork,reuseaddr EXEC:\""+socatExec+"\" &"]

    subprocess.call(cmdAttach + attachInstallSocat)
    subprocess.call(cmdAttach + onSh + attachSocat)

if __name__ == '__main__':
  main()

