# tcp_client.py
import socket
import time

HOST = "container_01" # Docker Compose creates an internal DNS for service names. So instead of using the IP you can just use the container name.
PORT = 5000

msg = "Hello over tcp\n"

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall(msg.encode("utf-8"))
        reply = s.recv(4096)
        break
    except ConnectionRefusedError:
        time.sleep(1)

print("Reply: ", reply.decode("utf-8", errors = "replace"))