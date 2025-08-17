# BOT SCURITY SYSTEM

Sebuah script Python sederhana untuk simulasi **proteksi domain/server** terhadap:
- IP mencurigakan
- Bypass attempt
- Serangan DDoS
- Pencarian bug/kelemahan server  

Hasil scan otomatis tersimpan di **security_log.txt** (UTF-8).

---

## ✨ Fitur
- ✅ Banner keren di terminal  
- ✅ Input domain atau IP server  
- ✅ Resolve domain ke IPv4/IPv6  
- ✅ Simulasi deteksi IP mencurigakan  
- ✅ Simulasi blok bypass & DDoS attack  
- ✅ Scan bug/kelemahan umum (SQLi, XSS, RCE, dll)  
- ✅ Export hasil ke file `security_log.txt`  

---

## 📦 Requirements

Pastikan sudah install:

- **Python 3.8+** (Windows/Linux/MacOS)  
- Modul Python standar (sudah ada bawaan)  

Opsional (jika ingin support DNS lebih advance):  
```bash
pip install dnspython

## Cara Install & Jalankan
```bash
git clone https://github.com/username/bot-scurity-system.git
cd bot-scurity-system
python bot-system.py

## Contoh ouput

```yaml
==================================================
   █▄▄ █▀█ ▀█▀   █▀ █▀▀ █░█ █▀█ █ █▄░█ █▀
   █▄█ █▄█ ░█░   ▄█ ██▄ █▀█ █▀▄ █ █░▀█ ▄█
==================================================
   BOT SCURITY SYSTEM
   Created by: s3t4n-01x
==================================================

Masukkan domain atau IP server: example.com

[✓] Target ditemukan: example.com -> 93.184.216.34

[*] Memeriksa aktivitas mencurigakan...
[!] Ditemukan IP mencurigakan: 192.168.1.10, 192.168.1.77, ...
[*] Memblokir bypass attempt...
[✓] Semua bypass attempt berhasil diblokir!
[*] Memeriksa serangan DDoS...
[!] DDoS Attack terdeteksi! Memblokir sumber serangan...
[✓] Serangan berhasil dinetralisir.
[*] Memindai bug/kelemahan domain/server...
[!] Potensi kelemahan terdeteksi: XSS, SQL Injection
[✓] Semua exploit berhasil diblokir.

[✔] Proses keamanan selesai. Target dalam status aman!

[💾] Hasil scan telah disimpan di file: security_log.txt


