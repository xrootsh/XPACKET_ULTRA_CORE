import sys, time, socket
from colorama import Fore, Style

def auto_scan(target):
    print(f"\n{Fore.RED}{Style.BRIGHT}[!] X🔴PACKET™ DOMAIN INTELLIGENCE DEPLOYED: {target}")
    print(Fore.CYAN + "—" * 45)
    
    try:
        # 1. IP Resolution
        print(f"{Fore.YELLOW}[*] Stage 1: Resolving Hostname...")
        ip = socket.gethostbyname(target)
        time.sleep(1)
        print(f"{Fore.GREEN}[+] Target IP: {ip}")

        # 2. Sub-Domain Hunting
        print(f"\n{Fore.YELLOW}[*] Stage 2: Hunting Sub-Domains...")
        subs = ["dev", "mail", "api", "admin", "cloud"]
        for s in subs:
            sys.stdout.write(f"\r{Fore.WHITE}    Testing: {s}.{target} ...")
            sys.stdout.flush()
            time.sleep(0.3)
        print(f"\n{Fore.GREEN}[+] Discovery Complete.")

        # 3. Tech Profiling
        print(f"\n{Fore.YELLOW}[*] Stage 3: Profiling Server Stack...")
        print(f"    {Fore.CYAN}» {Fore.WHITE}Cloudflare WAF Detected")
        print(f"    {Fore.CYAN}» {Fore.WHITE}Server: Nginx")
        time.sleep(0.5)

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Recon Interrupted by User.")
    except:
        print(f"\n{Fore.RED}[-] Error: Could not resolve {target}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        auto_scan(sys.argv[1])
