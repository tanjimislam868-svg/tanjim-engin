#!/bin/bash
# TANJIM PREMIUM ENGINE - AUTO INSTALLER

echo -e "\033[1;36m[+] Starting Auto-Setup for Termux...\033[0m"

# 1. Storage Permission & Install Dependencies
echo -e "\033[1;33m[+] Asking for Storage Permission...\033[0m"
termux-setup-storage
sleep 2

echo -e "\033[1;33m[+] Installing Python, Rust, and Clang (This takes time)...\033[0m"
pkg update -y && pkg upgrade -y
pkg install python python-pip rust clang binutils libffi openssl -y

# 2. Install Python Libraries
echo -e "\033[1;33m[+] Installing Python Libraries...\033[0m"
pip install curl_cffi cryptography

# 3. Run Script
echo -e "\033[1;32m[+] Setup Complete! Starting Engine...\033[0m"
clear
python main.py