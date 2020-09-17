
# This program scans the ports on the system and
# determines which ones are open. It also prints the
# time it took to complete.

import socket, sys
from datetime import datetime

# a function to check if the specified port is open
def check_port(host, port):
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        return False
    return True

# a function to check if the input host is valid
def valid_host(address):
    try:
        socket.inet_aton(address)
        return True
    except:
        return False

# if there are command line arguments, the first is used
# as the host. Otherwise, the host address is asked for.
# Must be in the form of a valid IPv4 address.
host = "a"
if len(sys.argv) > 1:
    host = sys.argv[1]
while valid_host(host) == False:
    host = input("Input host: ")

# if there is a second command line argument, it is used
# as the range. Should be in the form ##-###, as it is
# delimited by the hyphen. If the given argument is not
# valid input, all ports will be scanned.
if len(sys.argv) > 2:
    ranges = sys.argv[2].split('-')
    try:
        start = int(ranges[0])
        end = int(ranges[1])
        if start < 1 or start >= end or end > 65535:
            raise Exception()
    except (ValueError, Exception):
        start = 1
        end = 65535
else:
    start = 1
    end = 65535

print("Scanning ports from %s to %s...\n" % (str(start), str(end)))

t1 = datetime.now()
for port in range(start, end+1):
    if check_port(host, port):
        print("%s:\tPort %s is open" % (host, str(port)))
t2 = datetime.now()
elapsed_time = t2-t1
print("\nScan completed in: " + str(elapsed_time))
