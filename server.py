import socket

conn = socket.socket()
print ("Socket successfully created")
conn.bind(("localhost",9998))
print("socket binded")
conn.listen(3)
print("waiting for connection")


while True:
    c, addr = conn.accept()
    name = c.recv(1024).decode()
    print("Got connection from", name, addr)
    c.send(("Thanks for connecting").encode())
    c.close()
    break
