import requests
import sys
import time

def stealth_mission(target):
    print(f"\n[!] GHOST-X STEALTH MODE ACTIVE: {target}")
    url = f"https://crt.sh/?q={target}&output=json"
    try:
        r = requests.get(url, timeout=20)
        if r.status_code == 200:
            subs = sorted(set([e['name_value'] for e in r.json()]))
            for s in subs:
                print(s)
                sys.stdout.flush()
                time.sleep(1.5) # Stealth delay
    except: pass

if __name__ == "__main__":
    if len(sys.argv) > 1: stealth_mission(sys.argv[1])
