import sys, time, os
from colorama import Fore, Style

def collect_loot(target):
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}[!] LOOT COLLECTOR DEPLOYED ON: {target}")
    print(Fore.CYAN + "—" * 45)
    
    loot_items = [
        ("Shadow Files", "/etc/shadow", "CRITICAL"),
        ("Browser Database", "Login Data", "HIGH"),
        ("SSH Keys", "id_rsa", "HIGH"),
        ("Environment Vars", ".env", "MEDIUM")
    ]
    
    for name, item, risk in loot_items:
        print(f"{Fore.YELLOW}[*] Extracting {name} ({item})...")
        time.sleep(0.8)
        print(f"{Fore.GREEN}[+] {name} SECURED. [Risk: {risk}]")

    # Creating an evidence log
    evidence_path = f"evidence/loot_{target}.txt"
    with open(evidence_path, "w") as f:
        f.write(f"Loot Report for {target}\nStatus: Exfiltrated\n")
    
    print(Fore.CYAN + "—" * 45)
    print(f"{Fore.WHITE}[i] All data synced to: {Fore.GREEN}{evidence_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        collect_loot(sys.argv[1])
