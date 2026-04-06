# UDP Multi-Client Music Server

A Python-based client-server music distribution system that uses UDP socket programming to allow multiple clients to request and receive songs simultaneously over a virtual network.

## Features

* UDP-based communication using Python sockets
* Multiple clients supported using multithreading
* Displays available songs before selection
* Transfer progress percentage and packet count
* Supports same song request by multiple clients at the same time

## Technologies Used

* Python
* UDP Socket Programming
* VirtualBox
* Ubuntu Linux

## Project Structure

* `server.py` → Handles client requests and sends songs
* `client.py` → Requests songs and receives files
* `songs/` → Stores available audio files

## How to Run

### Server

```bash
python3 server.py
```

### Client

```bash
python3 client.py
```

## Network Configuration

* Server IP: `192.168.1.10`
* Clients: `192.168.1.11` to `192.168.1.15`
* Internal Network: `intnet`

## Output

Clients can view available songs, request a selected song, and receive it as a local audio file.

## Future Improvements

* Live audio streaming
* GUI interface
* Authentication system
* Packet recovery for improved reliability
