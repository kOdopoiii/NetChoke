# ⚡ NetChoke
**Network Traffic Control & Selective ARP Spoofing Tool.**

NetChoke adalah alat penelitian keamanan jaringan yang dirancang untuk mensimulasikan gangguan jaringan (Latency/Lag) dan pemutusan koneksi (DoS) secara selektif pada jaringan lokal.

## ✨ Fitur
- **Auto-Discovery**: Deteksi Gateway dan Interface secara otomatis.
- **Selective Targeting**: Pilih target spesifik berdasarkan IP/MAC.
- **Dual Mode**: 
  - `LAG Mode`: Mensimulasikan high-latency (ping spike).
  - `DC Mode`: Memutuskan koneksi target sepenuhnya.
- **Stealth UI**: Tampilan terminal yang bersih dan profesional.

## 🚀 Cara Instalasi
```bash
git clone [https://github.com/kOdopoiii/NetChoke.git](https://github.com/kOdopoiii/NetChoke.git)
cd NetChoke
chmod +x setup.sh
./setup.sh