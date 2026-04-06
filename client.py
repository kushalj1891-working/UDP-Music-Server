import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = "192.168.1.10"
port = 5000

client.sendto(b"LIST", (server_ip, port))

data, _ = client.recvfrom(4096)

print("\nAvailable Songs:")
print(data.decode())

song = input("\nEnter song name: ")

client.sendto(song.encode(), (server_ip, port))

filesize_data, _ = client.recvfrom(1024)

if filesize_data == b"Song not found":
    print("Song not found on server")
    exit()

filesize = int(filesize_data.decode())

filename = "received_" + song

received = 0
packet_count = 0

with open(filename, "wb") as f:
    while True:
        data, _ = client.recvfrom(1024)

        if data == b"END":
            break

        f.write(data)

        received += len(data)
        packet_count += 1

        progress = (received / filesize) * 100
        print(f"Progress: {progress:.2f}% | Packets: {packet_count}", end="\r")

print("\nSong received successfully")
print("Saved as:", filename)
print(f"Total packets received: {packet_count}")