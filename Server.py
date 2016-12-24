import socket

TCP_IP = '127.3.13.13'
TCP_PORT = 3033
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print "Listening..."

conn, addr = s.accept()
print "Connection address: ", addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "recieved data: ", data
	IPAddr = socket.gethostbyname(data)
	print "It's IP address is: ", IPAddr
	conn.send(IPAddr)
conn.close()
