import sys, threading, socket, os, subprocess

# --- X🔴PACKET™ MULTI-COLOR INTELLIGENCE ---
WORDLIST = "/root/xpacket_v10/SecLists/Discovery/DNS/bitquark-subdomains-top100000.txt"
THREADS = 100
OUTPUT_FILE = "~/XPACKET_ULTRA_CORE/found_subs.txt"

def check_sub(target, sub):
    fqdn = f"{sub.strip()}.{target}"
    sub_lower = sub.lower()
    
    try:
        socket.gethostbyname(fqdn)
        
        # --- CATEGORY LOGIC ---
        if any(k in sub_lower for k in ['vpn', 'sso', 'admin', 'auth', 'vault', 'login', 'root']):
            icon = "🔴 [CRITICAL]"
        elif any(k in sub_lower for k in ['mail', 'exchange', 'api', 'db', 'sql', 'docs']):
            icon = "🟠 [SENSITIVE]"
        elif any(k in sub_lower for k in ['dev', 'test', 'staging', 'demo', 'old', 'new']):
            icon = "🟡 [P-INTEREST]"
        elif any(k in sub_lower for k in ['blog', 'news', 'help', 'static', 'assets']):
            icon = "🔵 [INFO]"
        else:
            icon = "🟢 [ACTIVE]"
            
        print(f"{icon} {fqdn}")
        
        with open(OUTPUT_FILE, "a") as f:
            f.write(fqdn + "\n")
    except: pass

def launch(target):
    print(f"\n[!] X🔴PACKET™ GOD-MODE: INTELLIGENCE CATEGORIZATION ACTIVE")
    if not os.path.exists(WORDLIST): return
    with open(WORDLIST, "r") as f:
        words = f.read().splitlines()
        threads = []
        for w in words:
            t = threading.Thread(target=check_sub, args=(target, w))
            t.start()
            threads.append(t)
            if len(threads) >= THREADS:
                for th in threads: th.join()
                threads = []

if __name__ == "__main__":
    launch(sys.argv[1]) if len(sys.argv) > 1 else print("Target missing")
