import socket
import threading
import serial

HEADER = 64 # The first message sent to the server must be length 64 bytes
PORT = 5050
#SERVER = "10.145.0.1"
SERVER = socket.gethostbyname(socket.gethostname())
# When we bind our socket to an address, it needs to be in a tuple where:
#           (Server, Port in which that server is running off of)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#ser = serial.Serial('COM7', 9800, timeout=1)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                #ser.close()

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
            #ser.write(b'H')
    conn.close()
    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()

