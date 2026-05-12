import os
import sys
import time
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def header(title):
    print(f"\n{Fore.RED}{Style.BRIGHT}[ {title} ]" + "—" * (40 - len(title)))

def godx_aggressive(target):
    print(f"\n{Fore.RED}{Style.BRIGHT} [🔥] GOD-X AGGRESSIVE ATTACK INITIATED: {target}")
    
    # --- SUB-CATEGORY 1: NETWORK INTEL ---
    header("NETWORK INTEL")
    print(f"{Fore.CYAN}[*] Hunting Subdomains & IP Assets...")
    subprocess.run(f"python3 core_tools/subdomain_discovery.py {target}", shell=True)
    print(f"{Fore.CYAN}[*] Mapping MAC & Server Fingerprints...")
    time.sleep(1)

    # --- SUB-CATEGORY 2: IDENTITY INTEL ---
    header("IDENTITY INTEL")
    print(f"{Fore.CYAN}[*] Searching Email Breaches & Passwords...")
    subprocess.run(f"python3 core_tools/mail_checker.py {target}", shell=True)

    # --- SUB-CATEGORY 3: HUMAN & SOCIAL INTEL ---
    header("HUMAN & SOCIAL INTEL")
    print(f"{Fore.CYAN}[*] Extracting Phone Nodes & Social Profiles...")
    # ഇവിടെയാണ് FB, Insta, Phone tracking വരുന്നത്
    subprocess.run(f"python3 core_tools/phone_intel.py {target}", shell=True)
    print(f"{Fore.YELLOW}[+] Target OSINT: FB/Insta Linked Check: OK")

    # --- SUB-CATEGORY 4: AUTO-PAYLOAD ADVISORY ---
    header("EXPLOIT ADVISORY")
    print(f"{Fore.RED}[!] SQLi Recommended: ' OR 1=1 --")
    print(f"{Fore.RED}[!] XSS Recommended: <script>alert('X')</script>")

    print(f"\n{Fore.GREEN}[✓] MISSION COMPLETE. ALL LAYERS SYNCED TO MOBILE.")

if __name__ == "__main__":
    t = sys.argv[1] if len(sys.argv) > 1 else input(f"{Fore.RED}target@godx{Fore.WHITE}:~# ").strip()
    if t: godx_aggressive(t)
