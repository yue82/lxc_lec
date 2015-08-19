#! /usr/bin/python
# encode:utf-8
import subprocess
import sys
import json

def main():
    cmdHost = ["/bin/hostname"]
    cmdDate = ["/bin/date"]
    cmdSar = ["/usr/bin/sar", "1", "1"]
    cmdLoadAvg = ["/usr/bin/sar", "-q", "1", "1"]
    cmdFree = ["/usr/bin/free"]

    try:
        copHost = subprocess.check_output(cmdHost, stderr=subprocess.STDOUT)
        copDate = subprocess.check_output(cmdDate, stderr=subprocess.STDOUT)
        copSar = subprocess.check_output(cmdSar, stderr=subprocess.STDOUT)
        copLA = subprocess.check_output(cmdLoadAvg, stderr=subprocess.STDOUT)
        copFree = subprocess.check_output(cmdFree, stderr=subprocess.STDOUT)
    except subprocess.CallProcessError, (p):
        print 'subprocess.CalledProcessError: cmd:%s returncode:%s' % (p.cmd, p.returncode)
        sys.exit(1)
    
    rsltHost = copHost.strip()
    rsltDate = copDate.strip()
    rsltSar = copSar.strip().split("\n")[3].strip().split()
    rsltLoadAvg = copLA.strip().split("\n")[3].strip().split()
    rsltFree1 = copFree.strip().split("\n")[1].strip().split()
    rsltFree2 = copFree.strip().split("\n")[2].strip().split()
    
    rsltCpu = {
        "LoadAvg1":float(rsltLoadAvg[3]),
        "LoadAvg5":float(rsltLoadAvg[4]),
        "LoadAvg15":float(rsltLoadAvg[5]),
        "User":float(rsltSar[2]),
        "System":float(rsltSar[4]),
        "IOWait":float(rsltSar[5]),
        "Idle":float(rsltSar[7])
    }
    
    rsltMem = {
        "Total":float(rsltFree1[1]),
        "Used":float(rsltFree2[2]),
        "Free":float(rsltFree2[3])
    }
    
    objAll = json.dumps({
        "Hostname": rsltHost, 
        "Date":rsltDate,
        "CpuData": rsltCpu,
        "MemData":rsltMem
    })

    print 'HTTP/1.1 200 OK'
    print 'Content-Type: application/json'
    print 'Content-Length: {}'.format(len(objAll) + 1)
    print
    print objAll
    
if __name__ == '__main__':
  main()

