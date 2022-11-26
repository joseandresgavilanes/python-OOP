import socket

s = socket.socket()
print("socket created")

port = 9000

s.bind(("", port))
s.listen(5)


response = {"status": "success"}

while True:
    c, addr = s.accept()
    print("got connection ", addr)
    c.close()
    print("socket finished")
