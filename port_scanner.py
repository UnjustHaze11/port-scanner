import socket
import sys


AUTHORIZED_TARGETS = {
    "127.0.0.1",
    "localhost",
    "scanme.nmap.org"
}

TIMEOUT = 0.5


def validate_port(port_value):
    """Validate that a port number is within the valid TCP port range."""
    if port_value < 1 or port_value > 65535:
        raise ValueError("Port numbers must be between 1 and 65535.")


def scan_port(target_ip, port):
    """
    Attempt to connect to a single TCP port.

    Returns True if the port is open and False otherwise.
    """

    # Create an IPv4 TCP socket.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner_socket:
        scanner_socket.settimeout(TIMEOUT)

        # connect_ex() returns 0 when the connection succeeds.
        result = scanner_socket.connect_ex((target_ip, port))

        return result == 0


def scan_target(target, start_port, end_port):
    """Scan a range of TCP ports on an authorized target."""

    # Prevent scanning systems outside the assignment's authorized scope.
    if target.lower() not in AUTHORIZED_TARGETS:
        print("Error: This target is not authorized for this assignment.")
        print("Authorized targets:")
        print("  localhost")
        print("  127.0.0.1")
        print("  scanme.nmap.org")
        return

    try:
        validate_port(start_port)
        validate_port(end_port)

        if start_port > end_port:
            raise ValueError(
                "The starting port must be less than or equal to the ending port."
            )

        # Convert the hostname into an IPv4 address.
        target_ip = socket.gethostbyname(target)

        print(f"\nScanning target: {target}")
        print(f"IP address: {target_ip}")
        print(f"Port range: {start_port}-{end_port}")
        print("-" * 40)

        open_ports = []

        # Scan each port in the requested range.
        for port in range(start_port, end_port + 1):
            try:
                if scan_port(target_ip, port):
                    print(f"Port {port}: OPEN")
                    open_ports.append(port)

            except socket.error as error:
                print(f"Socket error while scanning port {port}: {error}")

        print("-" * 40)

        if open_ports:
            print(f"Open ports found: {open_ports}")
        else:
            print("No open ports were found in the selected range.")

    except socket.gaierror:
        print("Error: The hostname could not be resolved.")

    except ValueError as error:
        print(f"Input error: {error}")

    except KeyboardInterrupt:
        print("\nScan stopped by the user.")

    except Exception as error:
        print(f"Unexpected error: {error}")


def main():
    """Collect user input and start the port scan."""

    print("Python TCP Port Scanner")
    print("=======================")
    print("Authorized targets:")
    print("1. localhost")
    print("2. 127.0.0.1")
    print("3. scanme.nmap.org")

    try:
        target = input("\nEnter target: ").strip()

        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

        scan_target(target, start_port, end_port)

    except ValueError:
        print("Error: Ports must be entered as whole numbers.")

    except KeyboardInterrupt:
        print("\nProgram stopped by the user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
