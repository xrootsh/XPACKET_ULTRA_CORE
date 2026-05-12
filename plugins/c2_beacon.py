import sys
import socket

def start_listener(port=4444):
    print(f"[📡] C2 Beacon Active. Listening on port {port}...")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', port))
        s.listen(1)
        return f"SUCCESS: C2 Port {port} is OPEN and waiting for callback."
    except Exception as e:
        return f"ERROR: Could not bind C2 - {str(e)}"

if __name__ == "__main__":
    print(start_listener())
