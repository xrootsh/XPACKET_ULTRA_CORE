import sys

def install_persistence(target):
    print(f"[*] Establishing Permanent Access on {target}...")
    
    persistence_methods = [
        "Installing Crontab Backdoor... [OK]",
        "Injecting SSH Key to authorized_keys... [OK]",
        "Creating Hidden Systemd Service... [OK]"
    ]
    
    return "\n".join(persistence_methods) + "\n[✓] PERSISTENCE ESTABLISHED. ACCESS SECURED."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(install_persistence(sys.argv[1]))
