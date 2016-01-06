import re
import subprocess
import sys
fd = open("ip_list.txt","r")
ip_list = fd.readlines()
for ip in ip_list:
    try:
        ip = ip.strip("\n")
        ping = subprocess.Popen(["ping", "-n", "-c 30", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = ping.communicate()
        out_list = out.split("\n")[-3:-1]
        out = '\n'.join(out_list)
        out = "destination ip ping:"+ip+"\n"+out
        print out
    except subprocess.CalledProcessError:
        print "Couldn't get a ping"
