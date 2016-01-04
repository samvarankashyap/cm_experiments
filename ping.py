import re
import subprocess
import sys
if len(sys.argv)==2:
    website = sys.argv[1]
    try:
        ping = subprocess.Popen(["ping", "-n", "-c 5", website], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, error = ping.communicate()
        print out.split("\n")[-3:-1]
    except subprocess.CalledProcessError:
        print "Couldn't get a ping"
else:
    #print sys.argv
    print "invalid parameters"
