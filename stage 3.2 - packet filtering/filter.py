from scapy.all import *

def filter_favicon(packet):
    """
    Filters out packets that contain HTTP GET requests for favicon.ico.
    """
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors='ignore')
        if "GET /favicon.ico" in payload:
            return True
    return False

def capture_favicon_packets(interface="your_network_interface"):
    """
    Capture and display packets requesting favicon.ico.
    """
    print("Starting packet capture...")
    sniff(iface=interface, prn=lambda x: x.summary() if filter_favicon(x) else None)

if __name__ == "__main__":
    capture_favicon_packets(interface="Wi-Fi")
