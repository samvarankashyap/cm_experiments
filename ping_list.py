import re
import subprocess
import sys
import pdb
pdb.set_trace()
fd = open("ip_list.txt","r")
ip_list = fd.readlines()
for ip in ip_list:
    try:
        print "current ip running is"
        print ip
        out_file = open("out_file.txt","a")
        ip = ip.strip("\n")
        ip = ip.split(",")
        ipaddr = ip[0]
        ping = subprocess.Popen(["ping", "-n", "-c 30", ipaddr], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = ping.communicate()
        out_list = out.split("\n")[-3:-1]
        out = '\n'.join(out_list)
        #out = "\ndestination ip ping:"+ip+"\n"+out+"\n"
        out = "destination ip::"+ip[0]+"::"+ip[1]+"::"+ip[2]+"\n"+out+"\n"
        out_file.write(out)
        print out
        out_file.close()
    except subprocess.CalledProcessError:
        print "Couldn't get a ping"
