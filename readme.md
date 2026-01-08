# ⚡ NetChoke
> **Network Traffic Controller & Selective ARP Spoofing Tool.**

NetChoke adalah alat audit keamanan jaringan yang dikembangkan dengan Python dan Scapy. Alat ini memungkinkan administrator jaringan untuk mensimulasikan gangguan jaringan (latency) atau pemutusan koneksi secara selektif pada perangkat di jaringan lokal (LAN).

---

## ✨ Fitur Utama
- **🔍 Auto-Discovery**: Deteksi otomatis Gateway, Interface, dan Subnet.
- **🎯 Smart Scanning**: Pemindaian ARP agresif untuk menemukan semua perangkat aktif.
- **📱 Vendor Identification**: Identifikasi merk perangkat (Vivo, Xiaomi, Apple, dll).
- **🛠 Dual Mode**:
    - **LAG Mode**: Menciptakan latensi tinggi (ping spike) pada target.
    - **DC Mode**: Memutus koneksi internet target sepenuhnya.
- **🛡 Safe Exit**: Fitur pemulihan tabel ARP otomatis saat program dihentikan (Ctrl+C).

---

## 🚀 Panduan Instalasi

Pilih instruksi sesuai dengan terminal atau sistem operasi yang Anda gunakan:

### 1. 🐉 Kali Linux / Parrot OS / Ubuntu / Debian
```bash
# Update sistem
sudo apt update && sudo apt install git python3 python3-pip -y

# Clone repositori
git clone [https://github.com/kOdopoiii/NetChoke.git](https://github.com/kOdopoiii/NetChoke.git)
cd NetChoke

# Instal dependensi
pip3 install -r requirements.txt --break-system-packages

# Jalankan
sudo python3 main.py
