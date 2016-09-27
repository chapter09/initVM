#!/usr/bin/python
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
parser.add_argument("-f", "--host", dest="hostfile",
        help="read host list from file", metavar="FILE")
parser.add_argument("-s", "--src", dest="source",
        help="source file/directory", metavar="SRC")
parser.add_argument("-d", "--dst", dest="destination",
        help="destination file/directory", metavar="DST")
parser.add_argument("-x", "--args", dest="arguments",
        help="arguments for rsync", metavar="RS")

args = parser.parse_args()
if len(sys.argv) < 7:
   #print len(sys.argv)
   parser.print_help()
   parser.exit(0)

host_list = []

host_list_fd = open(args.hostfile)
#print host_list_fd

# regex for IPv4
pat = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

for line in host_list_fd.readlines():
    if not line.strip():
        continue
    m = re.search(pat, line)
    if m:
        print m.group(0).strip()
        host_list.append(m.group(0).strip())

host_list_fd.close()

local_addr = socket.gethostbyname(socket.gethostname())

for host in host_list:
    if host.strip() == local_addr.strip():
        continue
    cmd = "rsync -arz --exclude logs --exclude \'%s\' %s %s:%s"%(args.arguments, 
            args.source, host, args.destination)
    print cmd
    p = subprocess.Popen(cmd, shell=True)
    p.wait()

print "DONE"
