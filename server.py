import socket


HOST = "127.0.0.1"  # Localhost
PORT = 65432        # Port used by the server
BUFFER_SIZE = 1024  # Maximum amount of data to receive at one time


def start_server():
    """Create and start a TCP socket server."""

    # Create a TCP/IP socket using IPv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            # Allows the address to be reused shortly after the program stops
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Bind the socket to the specified IP address and port
            server_socket.bind((HOST, PORT))

            # Listen for incoming connections
            server_socket.listen()

            print(f"Server is listening on {HOST}:{PORT}...")

            # Accept a connection from a client
            connection, client_address = server_socket.accept()

            # Automatically close the client connection when finished
            with connection:
                print(f"Connected to client: {client_address}")

                # Receive data from the client
                data = connection.recv(BUFFER_SIZE)

                if data:
                    message = data.decode("utf-8")
                    print(f"Client message: {message}")

                    # Send a response back to the client
                    response = "Message received by the server."
                    connection.sendall(response.encode("utf-8"))

        except OSError as error:
            print(f"Server socket error: {error}")

        except Exception as error:
            print(f"Unexpected server error: {error}")


if __name__ == "__main__":
    start_server()
