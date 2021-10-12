import socket
import threading
from datetime import datetime

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")
    
    
    connected = True 
    while connected:
        msg_length = connection.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = connection.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT:
                connected = False
            print(f"[{address}] {msg}")
            now = datetime.now().strftime("%H:%M:%S")
            connection.send(f"Message received at {now}".encode(FORMAT))
            
    connection.close()

def start_server():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        connection.send(f"Welcome to the server {address[0]}! \n".encode(FORMAT))
        connection.send(f"Enter !DISCONNECT to exit the server.".encode(FORMAT))
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
        

print("[STARTING] server is starting...")
start_server()
