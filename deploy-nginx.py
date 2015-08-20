#! /usr/bin/python3
# encode:utf-8

def main():
    lxcApList = ["ubuntu-ap1", "ubuntu-ap2"]
    lxcNginxList = ["ubuntu-nginx"]
    apIpAddr = {}
    
    username = "ubuntu"
    lxcPath = "/var/lib/lxc/"
    lxcRoot = "/rootfs"

    # get Aps ip address
    for lxcName in lxcApList:
        apIpAddr[lxcName] = 00

    
    for lxcName in lxcNginxList:
        # nginx install
        insNginx = ["./aptget-lxc.py", "nginx", lxcName]
        subprocess.check_call(insNginx)

        # stop nginx service 


        # make location config

        # make upstream config

        # write configs

        # start nginx service


if __name__ == '__main__':
    main()
