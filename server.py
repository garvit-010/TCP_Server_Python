import socket

# Creating a socket

def socket_creation():
    try:
        global host
        global port 
        global s
        host = ""
        port = 8080
        s = socket.socket()

    except socket.error as msg:
        print(f"Error in creating a socket: {str(msg)}")
    
# Binding the socket

def bind_socket():
    try:
        global host
        global port 
        global s
        print(f"Binding the socket: {str(port)}")
        
        s.bind((host,port))
        s.listen(5)
    
    except socket.error as msg:
        print(f"Error in creating a socket: {str(msg)}\nRetrying.... ")
        bind_socket()


# Accepting the incoming signal

def accept_socket():
    conn, address = s.accept()

    print(f"Established connection with:\nIP Address = {address[0]}\nPort = {str(address[1])}")

    conn.close()

def main():
    socket_creation()
    bind_socket()
    accept_socket()

main()