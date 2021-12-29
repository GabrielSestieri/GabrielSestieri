import socket
import time
import threading

PORT = 5051
SERVER = "192.168.1.31"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client, msg):
    client.send(msg.encode())

def start():
    answer = input("Connect to the server? (y/n) ")
    if answer.lower() != "y":
        return

    connection = connect()
    username_status = False
    while not username_status:
        username = input("Enter username: ")
        fullname = input("Enter full name: ")
        if username != '':
            send(connection, username+"|"+fullname)
            username_status = True
        else:
            print("Username is required")
            username_status = False

    while True:
        msg = (input("Send a message: (q for quit): "))
        if msg == "q":
            break
        send(connection, msg)
    thread = threading.Thread(target=connect)
    thread.start()
    send(connection, DISCONNECT)
    time.sleep(1)
    print("Disconnected")

start()















