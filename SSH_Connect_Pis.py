#!/Desktop/

import subprocess
import sys

with open('network_info.py', 'r')as f:
        for line in f:
                for word in line.split():
                        network_info = []
                        network_info.append(word)
                        print(word)

for i, value in enumerate(network_info):
        network_info[i] = value.replace('(', '').replace(')', '')
print network_info[0]

HOST=network_info[0]
COMMAND="uname -a"

ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	shell=False,
	stdout=subprocess.PIPE,
	stderr=subprocess.PIPE)
result = ssh.stdout.readline()
if result == []:
	error = ssh.stderr.readlines()
	print >>sys.stderr, "ERROR: %s" % error
else:
	print result
