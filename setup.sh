#!/bin/bash

# Warna terminal
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}[*] NetChoke Setup Wizard${NC}"
echo -e "${CYAN}[*] ----------------------${NC}"

# 1. Update & Install Python pip jika belum ada
if ! command -v pip3 &> /dev/null
then
    echo -e "${RED}[!] pip3 tidak ditemukan. Menginstall...${NC}"
    sudo apt update && sudo apt install python3-pip -y
fi

# 2. Install library dari requirements.txt
echo -e "${GREEN}[*] Menginstall library Python (Scapy)...${NC}"
sudo pip3 install -r requirements.txt

# 3. Beri izin IP Forwarding
echo -e "${GREEN}[*] Mengaktifkan IP Forwarding di Kernel...${NC}"
sudo sysctl -w net.ipv4.ip_forward=1

# 4. Beri izin eksekusi pada file utama
chmod +x main.py

echo -e "${CYAN}[*] Setup Selesai!${NC}"
echo -e "${GREEN}[*] Gunakan perintah berikut untuk menjalankan:${NC}"
echo -e "${RED}sudo python3 main.py${NC}"