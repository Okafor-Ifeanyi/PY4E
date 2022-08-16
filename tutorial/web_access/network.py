import socket

# makes a connection to the domain listed
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('chinanya.xyz', 80))
cmd = "GET http:///index.html HTTP/1.0\n\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()