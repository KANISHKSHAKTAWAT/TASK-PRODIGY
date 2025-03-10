from scapy.all import sniff, IP, TCP, UDP
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama for colored output

# Function to process each captured packet
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        
        # Highlight suspicious packets (example logic)
        if "malicious" in str(packet):
            print(Fore.RED + f"⚠️  Suspicious Packet Detected! {src_ip} --> {dst_ip} | Protocol: {protocol}")
        else:
            print(Fore.GREEN + f"✅ {src_ip} --> {dst_ip} | Protocol: {protocol}")

        # Display payload data (if available)
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = bytes(packet[TCP].payload) if packet.haslayer(TCP) else bytes(packet[UDP].payload)
            print(f"Payload Data: {payload.decode(errors='ignore')}\n{'-'*50}")

# Sniff network packets
print(Fore.CYAN + "[*] Starting Packet Sniffer...")
sniff(prn=packet_callback, store=0)
