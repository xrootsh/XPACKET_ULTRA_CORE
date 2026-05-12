import os
import sys
import subprocess
import signal
import time
from colorama import Fore, Style, init

init(autoreset=True)

def signal_handler(sig, frame):
    print(f"\n{Fore.RED} [!] X🔴PACKET™ Vanished. Stay Shadow.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def master_header():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(" " * 43 + f"{Fore.WHITE}{Style.BRIGHT}TM")
    logo = [
        r"█   █ ████   ██   ████ █  █ ████ █████",
        r" █ █  █   █ █  █  █    █ █  █      █  ",
        r"  █   ████  ████  █    ██   ███    █  ",
        r" █ █  █     █  █  █    █ █  █      █  ",
        r"█   █ █     █  █  ████ █  █ ████   █  "
    ]
    for line in logo:
        print(" " * 5 + Fore.RED + Style.BRIGHT + line)
    print(Fore.WHITE + Style.BRIGHT + "  ULTRA  " + f"[ v133.0 | EST. 2026 | {Fore.CYAN}@xrootaccess{Fore.WHITE} ]")
    print(Fore.CYAN + "—" * 48)
    print(f" X🔴PACKET™ | STATUS: {Fore.GREEN}SYNCED{Fore.WHITE} | MODE: {Fore.LIGHTRED_EX}{Style.BRIGHT}AGGRESSIVE")
    print(Fore.CYAN + "—" * 48 + "\n")

def run_tool(cmd):
    try:
        subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW} [!] Interrupted. Returning to base...")

def main_menu():
    while True:
        master_header()
        print(" " * 13 + Fore.MAGENTA + Style.BRIGHT + "OFFENSIVE CONSOLE")
        print(Fore.WHITE + "  " + "—" * 44)
        
        modules = [
            ("[01]", "god-x [smart-detection]",  "READY"),
            ("[02]", "domain-osint [auto]",      "READY"),
            ("[03]", "mail-vuln [gmail check]",  "READY"),
            ("[04]", "insta-hunter [osint]",     "READY"),
            ("[05]", "mobile-intel [tracker]",   "READY"),
            ("[06]", "phantom [ghost-clean]",    "READY"),
            ("[07]", "x-infra [live-report]",    "ACTIVE"),
            ("[08]", "c2 dashboard [live]",      "NEURAL"),
            ("[09]", "wireless hunt [wifi]",     "ARMED"),
            ("[10]", "pdf report [gen]",         "READY"),
            ("[00]", "stop system",              "vanish")
        ]
        
        for cmd_num, name, status in modules:
            color = Fore.GREEN if status in ["READY", "ACTIVE"] else (Fore.CYAN if status == "NEURAL" else Fore.RED)
            print(f"  {Fore.YELLOW}{cmd_num} {Fore.WHITE}{name:<28} {color}[{status}]")
        print(Fore.WHITE + "  " + "—" * 44 + "\n")
        
        try:
            choice = input(Fore.RED + Style.BRIGHT + " root" + Fore.WHITE + "@" + Fore.GREEN + Style.BRIGHT + "xrootaccess" + Fore.WHITE + ":" + Fore.CYAN + "~" + Fore.WHITE + "# ").strip()
            
            if choice == '01':
                while True:
                    master_header()
                    print(f" " * 15 + f"{Fore.LIGHTRED_EX}{Style.BRIGHT}GOD-X INTELLIGENCE")
                    print(f"\n {Fore.WHITE}[#] ENTER TARGET {Fore.CYAN}(ip/domain/mail)")
                    print(f" {Fore.WHITE}[#] TYPE {Fore.LIGHTRED_EX}{Style.BRIGHT}0{Fore.WHITE} TO RTB")
                    target = input(f"\n {Fore.LIGHTRED_EX}{Style.BRIGHT}godx{Fore.WHITE}@{Fore.GREEN}xrootaccess{Fore.WHITE}:~# ").strip()
                    if target == '0' or target == '': break
                    run_tool(f"python3 core_tools/mass_striker.py {target}")
            
            elif choice == '08':
                print(f"\n{Fore.CYAN}[*] Starting C2 Neural Dashboard on port 8080...")
                run_tool("python3 dashboard.py")
            elif choice == '09':
                print(f"\n{Fore.RED}[!] Initializing Wireless Hacking Engine...")
                run_tool("python3 core_tools/x_check_infra.py") # Using your existing infra checker for now
            elif choice == '10':
                print(f"\n{Fore.GREEN}[*] Compiling PDF Security Report...")
                run_tool("python3 core_tools/vuln_analyzer.py --report")
            elif choice == '00':
                signal_handler(None, None)
            elif choice in ['02','03','04','05','06','07']:
                # Common mapping for other tools
                mapping = {'02':'domain_recon.py','03':'mail_checker.py','04':'social_hunter.py','05':'tracker.py','06':'cleaner.py','07':'cat core_tools/found_targets.txt'}
                if choice == '07': run_tool(mapping[choice]); input("\nPress Enter...")
                else: 
                    t = input(f"\n{Fore.YELLOW} [?] Target: ")
                    if t: run_tool(f"python3 core_tools/{mapping[choice]} {t}")

        except (KeyboardInterrupt, EOFError):
            signal_handler(None, None)

if __name__ == "__main__":
    main_menu()
