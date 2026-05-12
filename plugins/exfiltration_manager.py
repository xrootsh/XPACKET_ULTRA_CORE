import sys
import base64

def exfiltrate(target):
    print(f"[*] Targeting Sensitive Data for Exfiltration on {target}...")
    # Simulation of sensitive file identification
    files_to_steal = ["/etc/passwd", "/root/.ssh/id_rsa", "/var/www/html/.env"]
    
    encoded_files = []
    for f in files_to_steal:
        # Encoding logic to bypass basic deep packet inspection
        encoded_files.append(f"DATA_CHUNK_{base64.b64encode(f.encode()).decode()}")
    
    return "EXFILTRATED_CHUNKS:\n" + "\n".join(encoded_files)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(exfiltrate(sys.argv[1]))
