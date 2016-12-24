import socket

TCP_IP = '127.3.13.13'
TCP_PORT = 3033
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

toURL = raw_input("Enter the Website you'd like to obtain the IP Address of: ")

s.send(toURL)
data = s.recv(BUFFER_SIZE)
s.close()

print "The IP Address of this website is: ", data