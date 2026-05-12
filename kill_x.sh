#!/bin/bash
echo -e "\033[1;31m[*] Terminating all X-Packet Ultra Processes...\033[0m"
pkill -f python3
pkill -f xlauncher.py
pkill -f ultra_v133.py
echo -e "\033[1;32m[+] All processes killed. System Clean.\033[0m"
