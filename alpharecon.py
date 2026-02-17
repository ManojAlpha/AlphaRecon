import socket
import os
from colorama import Fore, Style, init

init(autoreset=True)

def ip_info():
    target = input(Fore.CYAN + "Enter domain: ")
    try:
        ip = socket.gethostbyname(target)
        print(Fore.GREEN + f"[+] IP Address: {ip}")
    except:
        print(Fore.RED + "[-] Unable to resolve domain")

def port_scan():
    target = input(Fore.CYAN + "Enter target IP: ")
    print(Fore.YELLOW + "Scanning ports 20-1024...")

    for port in range(20, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((target, port))
        if result == 0:
            print(Fore.GREEN + f"[+] Port {port} OPEN")
        s.close()

def system_info():
    print(Fore.MAGENTA + "[+] System Information")
    os.system("uname -a")
    os.system("whoami")
    os.system("ifconfig")

def main():
    while True:
        print(Fore.BLUE + """
        === AlphaRecon ===
        1. IP Info
        2. Port Scan
        3. System Info
        4. Exit
        """)

        choice = input(Fore.CYAN + "Select option: ")

        if choice == "1":
            ip_info()
        elif choice == "2":
            port_scan()
        elif choice == "3":
            system_info()
        elif choice == "4":
            print(Fore.RED + "Exiting AlphaRecon...")
            break
        else:
            print(Fore.RED + "Invalid option")

if __name__ == "__main__":
    main()
