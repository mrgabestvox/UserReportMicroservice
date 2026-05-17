import socket
import json

HOST = "127.0.0.1"
PORT = 5000

payload = {
    "user": "Player One",
    "service": "Interactive Novel",
    "report": "Completed Chapter Two with character Ezekiel."
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(json.dumps(payload).encode("utf-8"))

    response = client.recv(4096)
    print(response.decode("utf-8"))