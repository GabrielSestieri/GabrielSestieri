import socket
import threading
from datetime import *


PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"

ACTIVE_CLIENTS = {}
USERNAME_STATUS = {}
username = ""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")
    try:
        connected = True
        while connected:
            #GETS USERNAME
            with clients_lock:
                for c in clients:
                    ip = c.getpeername()[0]
                    if ip == address[0]:
                        if USERNAME_STATUS[ip] == False:
                            response = connection.recv(2048).decode('utf-8')
                            username = response.split("|")[0]
                            fullname = response.split("|")[1]
                            if username != '':
                                ACTIVE_CLIENTS[address[0]] = [username, fullname]
                                print(ACTIVE_CLIENTS)
                                USERNAME_STATUS[ip] = True
                                break
                            else:
                                print("Username is empty")
                        else:
                            break
            #GETS MESSAGES
            msg = connection.recv(2048).decode(FORMAT)
            if not msg:
                break
            if msg == DISCONNECT:
                connected = False
            with clients_lock:
                for c in clients:
                    ip = c.getpeername()[0]
                    user = ACTIVE_CLIENTS.get(str(ip))
                    time = datetime.now().strftime("%H:%M")
                    if msg == "show me":
                        print(ACTIVE_CLIENTS[ip])
                    if ip == address[0]:
                        print(f"[{time}] {user[0]}: {msg}")
            #RANDOM COMMENT                     
    finally:
        with clients_lock:
            clients.remove(connection)
        connection.close()

def start_server():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        with clients_lock:
            clients.add(connection)
            ACTIVE_CLIENTS[address[0]] = ""
            USERNAME_STATUS[address[0]] = False
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        connection.send(f"Welcome to the server {address[0]}! \n".encode(FORMAT))
        connection.send(f"Enter !DISCONNECT to exit the server.".encode(FORMAT))
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
        
print("[STARTING] server is starting...")
start_server()
