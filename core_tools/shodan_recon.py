import os
import sys
import json
import shodan
from colorama import Fore, Style, init

init(autoreset=True)

CONFIG_FILE = "~/XPACKET_ULTRA_CORE/X_DATABASE/shodan_config.json"

def get_api_key():
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get("api_key")
    except:
        return None

def shodan_scan(query):
    api_key = get_api_key()
    if not api_key:
        print(f"{Fore.RED}[!] Error: Shodan API Key not found in config.")
        return

    api = shodan.Shodan(api_key)
    print(f"\n{Fore.CYAN}[🌐] INITIATING SHODAN RECON: {query}")
    
    try:
        # ഐപി അഡ്രസ് ആണോ എന്ന് നോക്കുന്നു
        results = api.host(query)
        print(f"{Fore.GREEN}[+] Organization: {results.get('org', 'n/a')}")
        print(f"{Fore.GREEN}[+] Operating System: {results.get('os', 'n/a')}")
        print(f"{Fore.YELLOW}[*] Open Ports: {results['ports']}")
        
        for item in results['data']:
            print(f"{Fore.WHITE}[-3] Port: {item['port']} | Service: {item['transport']}")
            
    except Exception as e:
        print(f"{Fore.RED}[!] Shodan Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        shodan_scan(sys.argv[1])
    else:
        target = input(f"{Fore.RED}shodan@recon{Fore.WHITE}:~# ").strip()
        if target: shodan_scan(target)
