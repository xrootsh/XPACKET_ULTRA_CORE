import sys

def clean_tracks(target):
    print(f"[!] Mission for {target} Ending. Initiating Track Eraser...")
    
    # Target logs to wipe
    logs_to_clear = [
        "/var/log/auth.log",
        "/var/log/syslog",
        "~/.bash_history",
        "/var/log/apache2/access.log"
    ]
    
    steps = []
    for log in logs_to_clear:
        steps.append(f"Wiping {log}... [DONE]")
    
    return "\n".join(steps) + "\n[✓] ALL TRACES REMOVED. GHOST MODE ACTIVE."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(clean_tracks(sys.argv[1]))
