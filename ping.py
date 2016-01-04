import re
import subprocess
website = "www.google.com"
try:
    ping = subprocess.Popen(["ping", "-n", "-c 5", website], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, error = ping.communicate()
    print out.split("\n")[-3:-1]

except subprocess.CalledProcessError:
    print "Couldn't get a ping"
