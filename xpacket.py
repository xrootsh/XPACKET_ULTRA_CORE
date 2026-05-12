import os
import sys
import subprocess
import signal
import time
from colorama import Fore, Style, init

init(autoreset=True)

CORE_PATH = "/root/XPACKET_ULTRA_CORE/core_tools"

def master_header(show_status=True):
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # TM in Neon White - Your original measurement
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
    print(Fore.CYAN + "—" * 50)
    
    if show_status:
        branding_plain = f" {Fore.WHITE}{Style.BRIGHT}✖️🔴PACKET™"
        print(f"{branding_plain} | STATUS: {Fore.GREEN}SYNCED{Fore.WHITE} | MODE: {Fore.RED}AGGRESSIVE")
        print(Fore.CYAN + "—" * 50 + "\n")

def vanish_screen():
    # സ്ക്രീൻ ക്ലിയർ ചെയ്ത് Traceback മെസ്സേജുകൾ വരുന്നത് തടയുന്നു
    os.system('clear')
    master_header(show_status=False)
    
    X_LINK = f"{Style.BRIGHT}{Fore.WHITE}x.com/xrootsh"
    GIT_LINK = f"{Style.BRIGHT}{Fore.WHITE}github.com/xrootsh"
    HANDLE = f"{Style.BRIGHT}{Fore.CYAN}@xrootsh"
    STAY_SHADOW = f"{Fore.BLACK}{Style.BRIGHT}Stay Shadow." 
    
    print(f"\n{Fore.RED}{Style.BRIGHT} [!] {Fore.WHITE}✖️🔴PACKET™ {Fore.RED}Vanished. {STAY_SHADOW}")
    print(f"\n{Fore.WHITE} 𝕏 {X_LINK} {Fore.CYAN}| {Fore.WHITE}📡 {GIT_LINK}")
    print(f" {Fore.WHITE}Handle: {HANDLE}\n")
    sys.exit(0)

# സിഗ്നൽ ഹാൻഡ്‌ലർ - ഇതാണ് ആ എറർ വരാതെ നോക്കുന്നത്
def signal_handler(sig, frame):
    vanish_screen()

signal.signal(signal.SIGINT, signal_handler)

def run_tool(cmd):
    try:
        # Subprocess വഴി റൺ ചെയ്യുമ്പോൾ Interrupt Handle ചെയ്യുന്നു
        subprocess.run(cmd, shell=True, check=False)
    except KeyboardInterrupt:
        vanish_screen()
    except Exception:
        pass # മറ്റ് ചെറിയ എററുകൾ സ്കിപ്പ് ചെയ്യുന്നു

def godx_intelligent_menu():
    while True:
        master_header()
        print(" " * 15 + f"{Fore.LIGHTRED_EX}{Style.BRIGHT}GOD-X INTELLIGENCE")
        print(Fore.WHITE + "  " + "—" * 44)
        print(f"  {Fore.CYAN}[?] Select Attack Vector:")
        print(f"  {Fore.YELLOW}[01] {Fore.WHITE}USERNAME   {Fore.GREEN}(Insta/FB/Mail)")
        print(f"  {Fore.YELLOW}[02] {Fore.WHITE}DOMAIN     {Fore.GREEN}(Web Recon/IP)")
        print(f"  {Fore.YELLOW}[03] {Fore.WHITE}MAC ADDR   {Fore.GREEN}(WiFi/Hardware)")
        print(f"  {Fore.YELLOW}[04] {Fore.WHITE}FULL ATTACK{Fore.RED}(Aggressive Mode)")
        print(f"  {Fore.YELLOW}[00] {Fore.WHITE}BACK TO BASE")
        print(Fore.WHITE + "  " + "—" * 44 + "\n")
        
        choice = input(f" {Fore.RED}godx{Fore.WHITE}@{Fore.GREEN}xrootaccess{Fore.WHITE}:~# ").strip()
        if choice == '00': break
        elif choice in ['01','02','03','04']:
            target = input(f"\n {Fore.YELLOW}[#] Enter Target: ").strip()
            if target:
                run_tool(f"python3 {CORE_PATH}/mass_striker.py {target} --mode {choice}")
                input("\n[#] Done. Press Enter...")

def main_menu():
    while True:
        master_header()
        print(" " * 14 + Fore.MAGENTA + Style.BRIGHT + "OFFENSIVE CONSOLE")
        print(Fore.WHITE + "  " + "—" * 44)
        
        modules = [
            ("[01]", "god-x [intelligent-mode]",  "READY"),
            ("[02]", "ghost-x [stealth-scanner]", "READY"),
            ("[03]", "infra-recon [live-report]", "ACTIVE"),
            ("[04]", "striker [data-exfiltrate]", "READY"),
            ("[05]", "c2 dashboard [neural-link]", "NEURAL"),
            ("[06]", "domain-osint [automated]",  "READY"),
            ("[07]", "mail-vuln [exploit-check]", "READY"),
            ("[08]", "insta-hunter [osint-ops]",  "READY"),
            ("[09]", "mobile-intel [tracking]",   "READY"),
            ("[10]", "wireless hunt [wifi-ops]",  "ARMED"),
            ("[11]", "phantom [log-purger]",      "READY"),
            ("[00]", "stop system",               "vanish")
        ]
        
        for cmd_num, name, status in modules:
            color = Fore.GREEN if status in ["READY", "ACTIVE"] else (Fore.CYAN if status == "NEURAL" else Fore.RED)
            print(f"  {Fore.YELLOW}{cmd_num} {Fore.WHITE}{name:<28} {color}[{status}]")
        print(Fore.WHITE + "  " + "—" * 44 + "\n")
        
        try:
            choice = input(f" {Fore.RED}root{Fore.WHITE}@{Fore.GREEN}xrootaccess{Fore.WHITE}:{Fore.CYAN}~{Fore.WHITE}# ").strip()
            if choice == '00': vanish_screen()
            elif choice == '01': godx_intelligent_menu()
            elif choice in ['02','03','04','05','06','07','08','09','10','11']:
                mapping = {'02':'ghost.py','03':'infra.py','04':'striker.py','05':'c2.py','06':'osint.py','07':'mail.py','08':'insta.py','09':'mobile.py','10':'wifi.py','11':'phantom.py'}
                run_tool(f"python3 {CORE_PATH}/{mapping[choice]}")
                input("\n[#] Done. Press Enter...")
        except (KeyboardInterrupt, EOFError):
            vanish_screen()

if __name__ == "__main__":
    main_menu()
