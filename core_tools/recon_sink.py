import subprocess
import re
from colorama import Fore

class ReconSink:
    def __init__(self):
        print(f"{Fore.BLUE}[*] Recon-Sink Engine Initialized...")

    def scan_range(self, network_range, target_service):
        """
        നെറ്റ്‌വർക്കിൽ സ്കാൻ ചെയ്ത് വൾനറബിൾ ഐപി കണ്ടെത്തുന്നു.
        """
        print(f"{Fore.YELLOW}[?] Scanning {network_range} for {target_service}...")
        vulnerable_ips = []
        
        try:
            # Nmap ഉപയോഗിച്ച് വേർഷൻ സ്കാൻ ചെയ്യുന്നു
            cmd = f"nmap -sV --open -p 80,8080 {network_range}"
            output = subprocess.check_output(cmd.split(), text=True)
            
            # സർവീസ് പേരും ഐപിയും മാച്ച് ചെയ്യാൻ
            sections = output.split("Nmap scan report for ")
            for section in sections[1:]:
                ip = section.split()[0]
                if target_service.lower() in section.lower():
                    print(f"{Fore.GREEN}[+] VULNERABLE TARGET FOUND: {ip}")
                    vulnerable_ips.append(ip)
                    
            return vulnerable_ips
        except Exception as e:
            print(f"{Fore.RED}[!] Recon Error: {e}")
            return []
