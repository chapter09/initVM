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
parser.add_argument("-s", "--src-file", 
        help="source file/directory", default=None, metavar="SRC FILE")
parser.add_argument("-S", "--src-list", 
        help="source list file", default=None, metavar="SRC LIST")
parser.add_argument("-d", "--dst", dest="destination",
        help="destination file/directory", metavar="DST")
parser.add_argument("-x", "--args", dest="arguments",
        help="arguments for rsync", metavar="RS")

args = parser.parse_args()
if len(sys.argv) < 7:
    parser.print_help()
    parser.exit(0)

#### Build up dst host list ####

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
                print(m.group(0).strip())
                host_list.append(m.group(0).strip())
else:
    host_list.append(args.host)
#print host_list_fd

#### Build up src file list ####

src_list = []
if args.src_list and os.path.exists(args.src_list):
    with open(args.src_list) as src_list_fd:  
        for line in src_list_fd.readlines():
            src_list.append(line.strip())
elif args.src_file and os.path.exists(args.src_file):
    src_list.append(args.src_file) 
else:
    print("ERROR: SRC does not exist")
    parser.print_help()
    exit(0)

#### Skip the local host ####

try:
    local_hostname = socket.gethostname()
    local_addr = socket.gethostbyname(local_hostname)
except socket.error:
    print "Has not found the local hostname"
    local_addr = None
    local_hostname = None

proc_list = []
for host in host_list:
    if (local_addr and host.strip() == local_addr.strip()) or \
       (local_hostname and host.strip() == local_hostname.strip()):
        continue
    for src in src_list:
        cmd = "rsync -arzq --exclude logs --exclude \'%s\' %s %s:%s" % (
            args.arguments, src, host, args.destination)
        print(cmd)
        proc_list.append(subprocess.Popen(cmd, shell=True))

for p in proc_list:
    p.wait()

print("DONE")
