import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 3000))
dataRecieved = s.recv(128)
print("Aleatorio recibido: ")
print(dataRecieved)