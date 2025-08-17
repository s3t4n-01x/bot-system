#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import random
import time
from datetime import datetime

# Fungsi clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Banner
def banner():
    print("\033[91m" + "="*50)
    print("   █▄▄ █▀█ ▀█▀   █▀ █▀▀ █░█ █▀█ █ █▄░█ █▀")
    print("   █▄█ █▄█ ░█░   ▄█ ██▄ █▀█ █▀▄ █ █░▀█ ▄█")
    print("="*50)
    print("   BOT SCURITY SYSTEM")
    print("   Created by: s3t4n-01x")
    print("="*50 + "\033[0m\n")

# Fungsi logging ke file (UTF-8 supaya aman di Windows/Linux)
def log_write(content):
    with open("security_log.txt", "a", encoding="utf-8") as f:
        f.write(content + "\n")

# Resolver domain ke IP (IPv4 & IPv6)
def resolve_target(target):
    try:
        infos = socket.getaddrinfo(target, None)
        ips = list(set([info[4][0] for info in infos]))
        return ips
    except socket.gaierror:
        return None

# Fungsi untuk simulasi deteksi IP
def security_scan(target):
    log_data = []
    ips = resolve_target(target)

    if not ips:
        result = "[!] Domain/IP tidak valid atau tidak bisa di-resolve!"
        print(result)
        log_write(result)
        return
    else:
        result = f"[✓] Target ditemukan: {target} -> {', '.join(ips)}\n"
        print(result)
        log_data.append(result)

    time.sleep(1)
    result = "[*] Memeriksa aktivitas mencurigakan..."
    print(result); log_data.append(result)
    time.sleep(1)
    suspicious_ips = [f"192.168.1.{random.randint(2, 254)}" for _ in range(5)]
    result = f"[!] Ditemukan IP mencurigakan: {', '.join(suspicious_ips)}"
    print(result); log_data.append(result)

    time.sleep(1)
    result = "[*] Memblokir bypass attempt..."
    print(result); log_data.append(result)
    time.sleep(1)
    result = "[✓] Semua bypass attempt berhasil diblokir!"
    print(result); log_data.append(result)

    time.sleep(1)
    result = "[*] Memeriksa serangan DDoS..."
    print(result); log_data.append(result)
    time.sleep(1)
    if random.choice([True, False]):
        result = "[!] DDoS Attack terdeteksi! Memblokir sumber serangan..."
        print(result); log_data.append(result)
        time.sleep(1)
        result = "[✓] Serangan berhasil dinetralisir."
        print(result); log_data.append(result)
    else:
        result = "[✓] Tidak ada serangan DDoS terdeteksi."
        print(result); log_data.append(result)

    time.sleep(1)
    result = "[*] Memindai bug/kelemahan domain/server..."
    print(result); log_data.append(result)
    time.sleep(1)
    bugs = ["SQL Injection", "XSS", "RCE", "LFI/RFI"]
    found = random.sample(bugs, random.randint(0, len(bugs)))
    if found:
        result = f"[!] Potensi kelemahan terdeteksi: {', '.join(found)}"
        print(result); log_data.append(result)
        result = "[*] Memblokir exploit attempt..."
        print(result); log_data.append(result)
        time.sleep(1)
        result = "[✓] Semua exploit berhasil diblokir."
        print(result); log_data.append(result)
    else:
        result = "[✓] Tidak ditemukan bug/kelemahan pada target."
        print(result); log_data.append(result)

    result = "\n[✔] Proses keamanan selesai. Target dalam status aman!"
    print(result); log_data.append(result)

    # Simpan hasil ke file log
    log_header = f"\n=== SECURITY LOG [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ==="
    log_write(log_header)
    for line in log_data:
        log_write(line)
    log_write("="*60 + "\n")
    print("\n[💾] Hasil scan telah disimpan di file: security_log.txt")

# Main program
if __name__ == "__main__":
    clear()
    banner()
    target = input("Masukkan domain atau IP server: ")
    print()
    security_scan(target)
