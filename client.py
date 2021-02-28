import socket
import sys

HEADER = 64 # The first message sent to the server must be length 64 bytes
PORT = 5050
SERVER = "10.2.9.193"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


#send(f"{sys.argv[1]}")
send("H")
input()
send(DISCONNECT_MESSAGE)