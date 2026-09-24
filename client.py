import socket


HOST = "127.0.0.1"  # Server IP address
PORT = 65432        # Server port
BUFFER_SIZE = 1024  # Maximum amount of data to receive at one time


def start_client():
    """Create a TCP client and connect to the server."""

    # Create a TCP/IP socket using IPv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connect to the server
            print(f"Connecting to {HOST}:{PORT}...")
            client_socket.connect((HOST, PORT))

            print("Connected to the server.")

            # Message to send to the server
            message = "Hello from the client!"

            # Send the message as bytes
            client_socket.sendall(message.encode("utf-8"))
            print(f"Sent: {message}")

            # Receive the server's response
            response = client_socket.recv(BUFFER_SIZE)

            if response:
                print(f"Server response: {response.decode('utf-8')}")

        except ConnectionRefusedError:
            print(
                "Connection was refused. Make sure the server is running "
                "before starting the client."
            )

        except socket.timeout:
            print("The connection timed out.")

        except OSError as error:
            print(f"Client socket error: {error}")

        except Exception as error:
            print(f"Unexpected client error: {error}")


if __name__ == "__main__":
    start_client()
