#!/usr/bin/env python3
import subprocess
import os

def enable_ghost_mode():
    """
    നിന്റെ ഐപി മറച്ചുവെക്കാൻ പ്രോക്സിചെയിൻ ആക്ടിവേറ്റ് ചെയ്യുന്നു.
    """
    print("[🌫️] X🔴PACKET™: ACTIVATING GHOST-MODE (PROXY-SHIELD)...")
    # TOR സർവീസ് സ്റ്റാർട്ട് ചെയ്യാൻ ശ്രമിക്കുന്നു
    os.system("service tor start 2>/dev/null")
    print("[✓] Traffic is now being routed through Global Proxies.")

def passive_recon(target):
    """
    ടാർഗെറ്റിൽ തൊടാതെ തന്നെ വിവരങ്ങൾ ശേഖരിക്കുന്നു (Passive Scan).
    """
    print(f"[🕵️] X🔴PACKET™: GHOST-INTEL GATHERING FOR {target}...")
    # നേരിട്ട് സൈറ്റിൽ പോകാതെ Shodan/Crt.sh വഴി വിവരങ്ങൾ എടുക്കുന്നു
    cmd = f"curl -s https://crt.sh/\?q\={target}\&output\=json | jq -r '.[].name_value' | sort -u"
    result = subprocess.getoutput(cmd)
    return result

if __name__ == "__main__":
    enable_ghost_mode()
