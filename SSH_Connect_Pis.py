#!/Desktop/

import subprocess
import sys
from pexpect import pxssh


with open('network_info.py', 'r')as f:
        for line in f:
                for word in line.split():
                        network_info = []
                        network_info.append(word)
                        print(word)

for i, value in enumerate(network_info):
        network_info[i] = value.replace('(', '').replace(')', '')
print network_info[0]

#HOST=network_info[0]
#COMMAND="uname -a"

#ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
#	shell=False,
#	stdout=subprocess.PIPE,
#	stderr=subprocess.PIPE)
#result = ssh.stdout.readline()
#if result == []:
#	error = ssh.stderr.readlines()
#	print >>sys.stderr, "ERROR: %s" % error
#else:
#	print result

s = pxssh.pxssh()
if not s.login (network_info[0], 'pi', 'raspberry'):
    print "SSH session failed on login."
    print str(s)
else:
    print "SSH session login successful"
    s.sendline ('ls -l')
    s.prompt()         # match the prompt
    print s.before     # print everything before the prompt.
    s.logout()
