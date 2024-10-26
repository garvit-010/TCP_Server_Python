import socket

s = socket.socket()

host = "xxx.xxx.x.xx" # local ip address
port = 8080 # Must be same as that of server

s.connect((host,port))