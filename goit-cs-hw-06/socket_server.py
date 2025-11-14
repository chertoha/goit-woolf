import socket
import urllib.parse
from datetime import datetime
from pymongo import MongoClient

MONGO_HOST = "mongodb"
MONGO_PORT = 27017

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client.messages_db
collection = db.messages

def parse_data(data):
    parsed = urllib.parse.parse_qs(data)
    return {
        "date": datetime.now().isoformat(),
        "username": parsed.get("username", [""])[0],
        "message": parsed.get("message", [""])[0]
    }

def run_socket_server():
    host = "0.0.0.0"
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Socket server running on {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if data:
                    msg = parse_data(data.decode())
                    collection.insert_one(msg)
                    print("Saved:", msg)

if __name__ == '__main__':
    run_socket_server()
