Here’s a sample `README.md` file for your client-server programs:

```markdown
# Simple Client-Server Socket Program in Python

This project demonstrates a basic client-server communication setup using Python's `socket` library. The server listens on a specified port for incoming connections, while the client connects to the server and establishes a connection.

## Files
- **server.py**: Contains code for setting up the server that binds to a specified port, listens for incoming connections, and accepts connections from clients.
- **client.py**: Contains code for setting up the client that connects to the server using the specified IP address and port.

## Requirements
- Python 3.x

## Usage

### 1. Start the Server
Run `server.py` on the machine you want to use as the server.

```bash
python server.py
```

The server will:
- Create a socket and bind it to the specified port.
- Listen for incoming connections.
- Accept a connection from the client and display the IP address and port of the client.

### 2. Run the Client
Run `client.py` on the machine you want to use as the client. Make sure to update the `host` variable with the server's IP address before running the program.

```bash
python client.py
```

The client will:
- Connect to the server using the specified IP address and port.

> **Note**: The port number in `client.py` and `server.py` must match.

## Code Overview

### Server (`server.py`)
- **socket_creation()**: Initializes the socket with default parameters.
- **bind_socket()**: Binds the socket to a specified host and port and begins listening for incoming connections.
- **accept_socket()**: Accepts an incoming connection, displays the IP address and port of the client, and then closes the connection.

### Client (`client.py`)
- **Socket Creation**: A socket object is created, and the client attempts to connect to the server.
- **Host and Port Configuration**: Update the `host` variable with the server's IP address and ensure the `port` matches the server’s port.




 
