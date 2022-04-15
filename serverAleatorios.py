import nacl
from nacl.utils import random
import socket

#generacion de aleatorio que vamos a mandar
size = 128
buf = nacl.utils.random(size)
data = ''
for char in buf:
    data += char.encode('hex')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3000)) #port 3000
s.listen(5)
while True: #siempre estaremos escuchando nuevas conexiones
    client, address = s.accept()
    print("connection from address: ", address, " succesfully established")
    client.send(data)