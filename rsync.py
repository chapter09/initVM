#!/usr/bin/python
# Python2.7
import os
import sys
import subprocess
import argparse
import re
import socket

# argv[1] host lists
# argv[2] source file/directory
# argv[3] dest file/directory

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--host", dest="host",
        help="read host ip or read host list from file")
parser.add_argument("-s", "--src", dest="source",
        help="source file/directory", metavar="SRC")
parser.add_argument("-d", "--dst", dest="destination",
        help="destination file/directory", metavar="DST")
parser.add_argument("-x", "--args", dest="arguments",
        help="arguments for rsync", metavar="RS")

args = parser.parse_args()
if len(sys.argv) < 7:
    parser.print_help()
    parser.exit(0)

host_list = []
if os.path.exists(args.host):
    with open(args.host) as host_list_fd:  
        # regex for IPv4
        pat = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

        for line in host_list_fd.readlines():
            if not line.strip():
                continue
            m = re.search(pat, line)
            if m:
                print m.group(0).strip()
                host_list.append(m.group(0).strip())
else:
    host_list.append(args.host)
#print host_list_fd

try:
    local_addr = socket.gethostbyname(socket.gethostname())
except socket.error:
    print "Has not found the local hostname"
    local_addr = None

for host in host_list:
    if local_addr and host.strip() == local_addr.strip():
        continue
    cmd = "rsync -arz --exclude logs --exclude \'%s\' %s %s:%s"%(args.arguments, 
            args.source, host, args.destination)
    print cmd
    p = subprocess.Popen(cmd, shell=True)
    p.wait()

print "DONE"
