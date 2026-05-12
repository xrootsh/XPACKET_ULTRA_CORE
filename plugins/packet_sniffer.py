from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if packet.haslayer(TCP):
            print(f"[TCP] {ip_src} -> {ip_dst} | Port: {packet[TCP].dport}")

print("[*] X🌍PACKET™ Sniffer Started... Monitoring Traffic...")
sniff(prn=packet_callback, store=0)
