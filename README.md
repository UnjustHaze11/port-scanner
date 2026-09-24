# Port Scanner and Socket Examples

This repository contains a simple TCP server, a matching client, and a basic port scanner for authorized targets.

## Files

- `server.py` — starts a TCP server that listens on `127.0.0.1:65432`
- `client.py` — connects to the server and sends a sample message
- `port_scanner.py` — scans a range of TCP ports for allowed targets

## Run the server

```bash
python server.py
```

This will start the server and wait for a client connection.

## Run the client

Open a second terminal and run:

```bash
python client.py
```

The client will connect to the local server, send a message, and print the server response.

## Run the port scanner

```bash
python port_scanner.py
```

You will be prompted to enter:

- target: `localhost`, `127.0.0.1`, or `scanme.nmap.org`
- starting port
- ending port

Example:

```bash
Enter target: localhost
Enter starting port: 20
Enter ending port: 80
```

## Notes

- The server and client are intended for local testing on `127.0.0.1`.
- The port scanner only allows specific authorized targets to reduce misuse.
- Port scans should be performed only on systems you own or are explicitly authorized to test.
