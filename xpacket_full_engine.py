import requests
import sys
import threading
import socket
import os
import time
import subprocess

# --- CONFIGURATION ---
WORDLIST = "/root/xpacket_v10/SecLists/Discovery/DNS/bitquark-subdomains-top100000.txt"
THREADS = 50
TOR_PROXY = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}
OUTPUT_FILE = "found_subs.txt"

class XPacketEngine:
    def __init__(self, target):
        self.target = target
        self.found_list = []
        self.lock = threading.Lock()

    def check_tor(self):
        try:
            r = requests.get("https://checkip.amazonaws.com", proxies=TOR_PROXY, timeout=10)
            print(f"[!] GHOST MODE ACTIVE. EXIT NODE IP: {r.text.strip()}")
            return True
        except:
            print("[!] TOR NOT DETECTED. PROCEEDING WITHOUT MASKING...")
            return False

    def scan_subdomain(self, sub):
        fqdn = f"{sub.strip()}.{self.target}"
        try:
            socket.gethostbyname(fqdn)
            with self.lock:
                if fqdn not in self.found_list:
                    print(f"[+] DISCOVERED: {fqdn}")
                    self.found_list.append(fqdn)
                    with open(OUTPUT_FILE, "a") as f:
                        f.write(fqdn + "\n")
        except:
            pass

    def start_discovery(self):
        print(f"\n[*] PHASE 1: AGGRESSIVE DISCOVERY ON {self.target}")
        if os.path.exists(WORDLIST):
            with open(WORDLIST, "r", encoding="utf-8", errors="ignore") as f:
                words = f.read().splitlines()
            
            threads = []
            for word in words:
                t = threading.Thread(target=self.scan_subdomain, args=(word,))
                t.start()
                threads.append(t)
                if len(threads) >= THREADS:
                    for th in threads: th.join()
                    threads = []
        else:
            print("[!] WORDLIST MISSING.")

    def start_web_eye(self):
        print(f"\n[*] PHASE 2: WEB-EYE TECHNOLOGY ANALYSIS")
        print("-" * 60)
        if os.path.exists(OUTPUT_FILE):
            cmd = f"httpx-toolkit -l {OUTPUT_FILE} -title -status-code -tech-detect -silent"
            subprocess.run(cmd.split())
        else:
            print("[!] NO SUBS FOUND TO ANALYZE.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 xpacket_full_engine.py <domain>")
        sys.exit()

    target_domain = sys.argv[1]
    engine = XPacketEngine(target_domain)
    engine.check_tor()
    try:
        engine.start_discovery()
    except KeyboardInterrupt:
        print("\n[!] DISCOVERY STOPPED BY USER. STARTING WEB-EYE ON CURRENT RESULTS...")
    
    engine.start_web_eye()
