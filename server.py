import socket
import os
import threading
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 5000))

songs_folder = "songs"

print("Advanced UDP Music Server Running...")

def handle_client(request, addr):
    if request == "LIST":
        songs = os.listdir(songs_folder)
        song_list = "\n".join(songs)
        server.sendto(song_list.encode(), addr)
        print(f"Song list sent to {addr}")

    else:
        filepath = os.path.join(songs_folder, request)

        if os.path.exists(filepath):
            filesize = os.path.getsize(filepath)

            server.sendto(str(filesize).encode(), addr)

            print(f"{addr} requested {request}")
            print(f"File size: {filesize} bytes")

            packet_count = 0

            with open(filepath, "rb") as f:
                while True:
                    chunk = f.read(1024)

                    if not chunk:
                        break

                    server.sendto(chunk, addr)
                    packet_count += 1
                    time.sleep(0.001)

            server.sendto(b"END", addr)

            print(f"{request} sent successfully to {addr}")
            print(f"Packets sent: {packet_count}")

        else:
            server.sendto(b"Song not found", addr)
            print(f"{addr} requested unavailable song")

while True:
    data, addr = server.recvfrom(1024)
    request = data.decode()

    client_thread = threading.Thread(target=handle_client, args=(request, addr))
    client_thread.start()