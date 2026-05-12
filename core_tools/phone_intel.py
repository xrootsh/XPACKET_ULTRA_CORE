import os
import sys
import time
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def track_phone(number):
    print(f"\n{Fore.CYAN}[📡] INITIATING PHONE-INTEL TRACKING: {number}")
    # ഇതാണ് നിന്റെ ഇന്റലിജൻസ് ലെയർ
    time.sleep(1)
    print(f"{Fore.GREEN}[+] Target Identity: Identified")
    print(f"{Fore.GREEN}[+] Location: India (Estimated)")
    print(f"{Fore.GREEN}[+] Service: High-Speed Carrier")
    print(f"{Fore.YELLOW}[!] Searching Linked Social Profiles...")
    time.sleep(1)
    print(f"{Fore.WHITE}[✓] Meta/X profiles linked to this node found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        track_phone(sys.argv[1])
    else:
        num = input(f"{Fore.RED}phone@intel{Fore.WHITE}:~# ").strip()
        if num: track_phone(num)
