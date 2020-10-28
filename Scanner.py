import socket
import sys
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid amount of arguments")
    print("syntx:python3 scanner <ip>")

print("_" * 50)
print("scanning targets "+target)
print("time started at "+str(datetime.now()))
print("_" * 50)
try:
    for port in range(1,8500):
        s = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print('port {} is open'.format(port))
        s.close()
except KeyboardInterrupt:
    print("\n exiting programme")
    sys.exit()

except socket.gaierror:
    print("no host")
    sys.exit()
    
except socket.error:
    print("cannont connect to server")
    sys.exit

