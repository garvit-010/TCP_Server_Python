# Simple Client-Server Socket Application

## Overview
This project demonstrates a basic client-server communication setup using Python's socket programming. The server listens for incoming connections on a specified port, while the client connects to the server using its IP address and the same port.

## Components
- **Server**: Listens for incoming connections and accepts client requests. It displays the IP address and port of the connecting client.
- **Client**: Connects to the server using a specified IP address and port, establishing a communication channel.

## Features
- Supports basic connection establishment between client and server.
- Displays the client’s IP address and port upon successful connection.

## Requirements
- Python 3.x must be installed on your machine.
- Familiarity with basic networking concepts can be helpful.

## Usage
1. **Start the Server**: Run the server program on the desired machine.
2. **Connect the Client**: Run the client program, ensuring the IP address of the server is correctly specified.

## Important Notes
- Ensure that the client and server are configured to use the same port.
- The server must be running before the client attempts to connect.
- The client is assigned a random port by the operating system for the duration of the connection.


