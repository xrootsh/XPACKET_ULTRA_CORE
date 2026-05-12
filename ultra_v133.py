import os
import sys
import subprocess
import signal
import time
import json
from colorama import Fore, Style, init

init(autoreset=True)

# Path Configuration
CONFIG_PATH = os.path.expanduser("~/XPACKET_ULTRA/core_tools/config.json")
EXFIL_SCRIPT = os.path.expanduser("~/XPACKET_ULTRA/core_tools/x_exfil_mail.py")
SIGN_OFF = f"{Fore.CYAN}X x.com/xrootsh {Fore.WHITE}| {Fore.CYAN}GitHub: github.com/xrootsh {Fore.WHITE}| {Fore.CYAN}Handle: @xrootsh"

def signal_handler(sig, frame):
    master_header()
    print(f"\n{Fore.RED}{Style.BRIGHT} [!] X🔴PACKET™ Vanished. Stay Shadow.")
    print(f"\n {SIGN_OFF}\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def save_config(db_type, mode="NORMAL"):
    config = {"active_db": db_type, "mode": mode, "sync_time": time.ctime()}
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)

def master_header():
    os.system('clear')
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
    print(Fore.WHITE + Style.BRIGHT + "  ULTRA  " + f"[ v133.0.1 | EST. 2026 | {Fore.CYAN}@xrootaccess{Fore.WHITE} ]")
    print(Fore.CYAN + "—" * 48)
    print(f" X🔴PACKET™ | STATUS: {Fore.GREEN}SYNCED{Fore.WHITE} | {Fore.RED}{Style.BRIGHT}MODE: AGGRESSIVE")
    print(Fore.CYAN + "—" * 48 + "\n")

def run_tool(cmd):
    try:
        subprocess.run(cmd, shell=True)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW} [!] Interrupted by user.")

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
            ("[10]", "exfil report [mail]",      "AUTO"),
            ("[11]", "master wordlists [sync]",  "MASTER"),
            ("[00]", "stop system",              "vanish")
        ]

        for cmd_num, name, status in modules:
            color = Fore.GREEN if status in ["READY", "ACTIVE", "AUTO"] else (Fore.CYAN if status == "NEURAL" else Fore.RED)
            print(f"  {Fore.YELLOW}{cmd_num} {Fore.WHITE}{name:<28} {color}[{status}]")
        print(Fore.WHITE + "  " + "—" * 44 + "\n")

        try:
            choice = input(Fore.RED + Style.BRIGHT + " root" + Fore.WHITE + "@" + Fore.GREEN + Style.BRIGHT + "xrootaccess" + Fore.WHITE + ":" + Fore.CYAN + "~" + Fore.WHITE + "# ").strip()

            if choice == '01':
                while True:
                    master_header()
                    print(f" " * 15 + f"{Fore.LIGHTRED_EX}{Style.BRIGHT}GOD-X INTELLIGENCE")
                    target = input(f"\n {Fore.LIGHTRED_EX}godx{Fore.WHITE}@{Fore.GREEN}xrootaccess{Fore.WHITE}:~# ").strip()
                    if target == '0' or target == '': break
                    run_tool(f"python3 core_tools/mass_striker.py {target}")

            elif choice == '11':
                while True:
                    master_header()
                    print(f" " * 12 + f"{Fore.YELLOW}{Style.BRIGHT}MASTER WORDLIST HUB")
                    print(f" [A] Passwords (RockYou)  [B] Discovery (SecLists)")
                    print(f" [V] VIEW/OPEN LISTS      [0] BACK")
                    sub = input(f"\n {Fore.RED}db{Fore.WHITE}@{Fore.GREEN}sync{Fore.WHITE}:~# ").upper().strip()
                    if sub == '0' or sub == '': break
                    if sub == 'V':
                        run_tool("ls -lh ~/XPACKET_ULTRA/X_DATABASE/MASTER_WORDLISTS/")
                        f = input("\n File to open: ").strip()
                        if f: run_tool(f"less ~/XPACKET_ULTRA/X_DATABASE/MASTER_WORDLISTS/{f}")
                    elif sub in ['A','B']:
                        save_config(sub)
                        print(f"{Fore.GREEN}[✓] Database Locked.")
                        time.sleep(1); break

            elif choice == '10':
                print(f"\n{Fore.GREEN}[*] Exfiltrating to xrootaccess@gmail.com...")
                run_tool(f"python3 {EXFIL_SCRIPT} 'ULTRA_REPORT' 'core_tools/found_targets.txt'")
                input("\n[#] Press Enter to return...")

            elif choice == '00':
                signal_handler(None, None)

            elif choice in ['02','03','04','05','06','07','08','09']:
                print(f"\n{Fore.CYAN}[*] Launching Module {choice}...")
                time.sleep(1)

        except (KeyboardInterrupt, EOFError):
            signal_handler(None, None)

if __name__ == "__main__":
    main_menu()
