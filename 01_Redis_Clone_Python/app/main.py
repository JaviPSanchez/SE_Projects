import socket  # noqa: F401
import sys

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    
    # 1) Create Server Socket to the address 127.0.0.1 and port 6379
    if sys.platform == "win32":
        # SO_REUSEPORT is not supported on Windows, so we omit it
        server_socket = socket.create_server(("localhost", 6379))
    else:        
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
        
        
    print("Server is waiting for a connection...")
    
    # 2) Accept a client connection, .accept method give as two objects:
    connection, address = server_socket.accept() # wait for client
    
    print(f"Connection established with {connection} and address {address}")
    
    # 3) Receive a request, the server listens for data from the client (buffer size 1024 bytes)
    with connection:
        request_data = connection.recv(1024)
        print(f"Received data: {request_data.decode()}")
    
        # 4) Send a response: The server sends data (a response) back to the client.
        response = "+PONG\r\n"
        # Send the response back to the client
        connection.send(response.encode())
    
        # 5) Close the connection: After responding, the server closes the client connection.
        connection.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
