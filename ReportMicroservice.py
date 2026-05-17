import socket
import json
from pathlib import Path
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 4096

def safe_filename(name):
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    cleaned = "".join(char for char in name if char in allowed)

    if not cleaned:
        raise ValueError("Invalid service name")

    return cleaned + ".txt"

def handle_client(connection):
    data = connection.recv(BUFFER_SIZE)

    if not data:
        return

    payload = json.loads(data.decode("utf-8"))

    user = payload["user"]
    service = payload["service"]
    report = payload["report"]

    filename = safe_filename(service)

    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')}\n")
        file.write(f"User: {user}\n")
        file.write(f"Service: {service}\n")
        file.write(f"Report: {report}\n")
        file.write("-" * 40 + "\n")

    connection.sendall(b"Report received.\n")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()

        print(f"Server listening on {HOST}:{PORT}")

        while True:
            connection, address = server.accept()

            with connection:
                print(f"Connected by {address}")
                try:
                    handle_client(connection)
                except Exception as error:
                    print(f"Error: {error}")
                    connection.sendall(b"Invalid request.\n")

if __name__ == "__main__":
    main()