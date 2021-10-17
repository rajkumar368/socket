import socket

conn = socket.socket()

conn.connect(("localhost", 9998))
name = input("name please")
conn.send((name).encode())
print(conn.recv(1024).decode())
conn.close()


