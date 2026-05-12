import sys
import os

def scan_local_net():
    print("[🖧] Scanning Internal Network for Lateral Movement...")
    # Using system ping to find live hosts in common subnets
    live_hosts = []
    # This is a focused scan on common internal ranges
    for i in range(1, 10): # Example range
        ip = f"192.168.1.{i}"
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        if response == 0:
            live_hosts.append(ip)
    return f"LIVE_INTERNAL_HOSTS: {', '.join(live_hosts)}" if live_hosts else "No other internal hosts found."

if __name__ == "__main__":
    print(scan_local_net())
