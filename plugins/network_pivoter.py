import socket
import os

def check_lateral_path(ip_range):
    print(f"[*] X🔴PACKET™ Pivot Engine: Scanning for Lateral Paths in {ip_range}...")
    
    # പ്രധാനപ്പെട്ട പോർട്ടുകൾ: 445 (SMB), 3389 (RDP), 22 (SSH)
    # ഇവയാണ് ഒരു സിസ്റ്റത്തിൽ നിന്ന് മറ്റൊന്നിലേക്ക് കടക്കാൻ ഹാക്കർമാർ ഉപയോഗിക്കുന്നത്.
    target_ports = [22, 445, 3389, 80, 443]
    
    # Example: 192.168.1.1 മുതൽ 1.254 വരെ
    base_ip = ".".join(ip_range.split('.')[:-1]) + "."
    
    for i in range(1, 255):
        target_ip = base_ip + str(i)
        for port in target_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.01) # അതിവേഗ സ്കാനിംഗ്
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"[🔥] LATERAL PATH FOUND: {target_ip} Port: {port}")
                # ഇവിടെ നമുക്ക് നമ്മുടെ 'phantom_injector' അല്ലെങ്കിൽ 'hardened_striker' 
                # ഓട്ടോമാറ്റിക് ആയി അങ്ങോട്ട് പുഷ് ചെയ്യാനുള്ള ലോജിക് ആഡ് ചെയ്യാം.
            sock.close()

if __name__ == "__main__":
    # നിന്റെ ലോക്കൽ നെറ്റ്‌വർക്ക് ഐപി റേഞ്ച് ഇവിടെ നൽകുക
    check_lateral_path("192.168.1.1")
