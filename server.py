import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen()

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

print("Server running...")

while True:
    client, addr = server.accept()
    print(f"Connected: {addr}")
    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()