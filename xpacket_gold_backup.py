import os
import sys
import subprocess
import signal
import time
import requests
from colorama import Fore, Style, init

init(autoreset=True)

# --- TELEGRAM C2 CONFIGURATION ---
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE" 
CHAT_ID = "YOUR_CHAT_ID_HERE"
CORE_PATH = "~/XPACKET_ULTRA_CORE/core_tools"
SIGN_OFF = f"{Fore.CYAN}X x.com/xrootsh {Fore.WHITE}| {Fore.CYAN}GitHub: github.com/xrootsh {Fore.WHITE}| {Fore.CYAN}Handle: @xrootsh"

def send_tg(message):
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                      data={"chat_id": CHAT_ID, "text": message})
    except: pass

def signal_handler(sig, frame):
    master_header()
    send_tg("⚠️ X🔴PACKET™: Terminal Session Terminated.")
    print(f"\n{Fore.RED}{Style.BRIGHT} [!] X🔴PACKET™ Vanished. Stay Shadow.")
    print(f"\n {SIGN_OFF}\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def master_header():
    os.system('clear')
    # കൃത്യമായ പഴയ TM പൊസിഷൻ
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
    print(Fore.WHITE + Style.BRIGHT + "  ULTRA  " + f"[ v133.0.1 | EST. 2026 | MOBILE-SYNCED 📲 ]")
    print(Fore.CYAN + "—" * 48)
    print(f" X🔴PACKET™ | STATUS: {Fore.GREEN}SYNCED{Fore.WHITE} | {Fore.RED}{Style.BRIGHT}MODE: AGGRESSIVE")
    print(Fore.CYAN + "—" * 48 + "\n")

def run_tool(script, args=""):
    path = os.path.join(CORE_PATH, script)
    subprocess.run(f"python3 {path} {args}", shell=True)

def godx_sub_menu():
    while True:
        master_header()
        print(" " * 13 + Fore.MAGENTA + Style.BRIGHT + "GOD-X PRIMARY WEAPON")
        print(Fore.WHITE + "  " + "—" * 44)
        print(f"  {Fore.YELLOW}[01] {Fore.WHITE}{'FULL AGGRESSIVE STRIKE':<28} {Fore.RED}[ALL-IN-ONE]")
        print(f"  {Fore.YELLOW}[02] {Fore.WHITE}{'NETWORK & INFRA SECTOR':<28} {Fore.CYAN}[IP/SUB/MAC]")
        print(f"  {Fore.YELLOW}[03] {Fore.WHITE}{'IDENTITY & BREACH SECTOR':<28} {Fore.CYAN}[MAIL/PASS]")
        print(f"  {Fore.YELLOW}[04] {Fore.WHITE}{'HUMAN & SOCIAL OSINT':<28} {Fore.CYAN}[MOBILE/FB]")
        print(f"  {Fore.YELLOW}[99] {Fore.RED}{'BACK TO MAIN CONSOLE':<28} {Fore.RED}[return]")
        print(Fore.WHITE + "  " + "—" * 44 + "\n")
        
        choice = input(Fore.RED + Style.BRIGHT + " root" + Fore.WHITE + "@" + Fore.RED + Style.BRIGHT + "godx" + Fore.WHITE + ":" + Fore.CYAN + "~" + Fore.WHITE + "# ").strip()
        
        if choice == '01':
            t = input(f"\n target@godx:~# ").strip()
            if t: run_tool("mass_striker.py", t)
            input("\n[#] Press Enter...")
        elif choice == '99': break

def main_menu():
    send_tg("🚀 X🔴PACKET™ Online: Mobile Connection Established.")
    while True:
        master_header()
        print(" " * 13 + Fore.MAGENTA + Style.BRIGHT + "OFFENSIVE CONSOLE")
        print(Fore.WHITE + "  " + "—" * 44)
        
        # സിങ്ക് ചെയ്ത ഫൈനൽ 5 ഓപ്ഷനുകൾ
        modules = [
            ("[01]", "god-x intelligence",      "READY"),
            ("[02]", "ghost-ops [stealth]",     "READY"),
            ("[03]", "infra-recon [shodan]",    "ACTIVE"),
            ("[04]", "strike-force [exploit]",  "ARMED"),
            ("[05]", "exfil & purge [clean]",   "AUTO"),
            ("[00]", "stop system",              "vanish")
        ]

        for cmd_num, name, status in modules:
            print(f"  {Fore.YELLOW}{cmd_num} {Fore.WHITE}{name:<28} {Fore.GREEN}[{status}]")
        print(Fore.WHITE + "  " + "—" * 44 + "\n")

        try:
            choice = input(Fore.RED + Style.BRIGHT + " root" + Fore.WHITE + "@" + Fore.GREEN + Style.BRIGHT + "xrootaccess" + Fore.WHITE + ":" + Fore.CYAN + "~" + Fore.WHITE + "# ").strip()

            if choice == '00': signal_handler(None, None)
            elif choice == '01': godx_sub_menu()
            elif choice == '02': run_tool("ghost_scanner.py")
            elif choice == '03': 
                t = input(f"\n target@shodan:~# ").strip()
                if t: run_tool("shodan_recon.py", t)
            elif choice == '04':
                t = input(f"\n target@strike:~# ").strip()
                if t: run_sync("payload_striker.py", t)
            elif choice == '05':
                print(f"{Fore.CYAN}[*] Sending Reports & Wiping Logs...")
                run_tool("x_exfil_mail.py")
                run_tool("cleaner.py")
                send_tg("📊 Mission Reports Sent. Logs Purged.")
                input("\n[#] Press Enter...")
        except:
            signal_handler(None, None)

if __name__ == "__main__":
    main_menu()
