import socket


s = socket.socket()

HOST = '142.197.50.50'
PORT = 4200

s.bind((HOST, PORT))
s.listen(5)

while True:
    client, address = s.accept()

    print(f'Connection from {address} has been established.')

    while True:
        LETTER = client.recv(1)
        SIZE = ord(LETTER.decode('utf-8'))
        msg = client.recv(SIZE)
        
    client.close()        