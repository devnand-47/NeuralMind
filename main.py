import sys
from colorama import Fore, Style, init
from modules.cortex import Cortex
from modules.ghost import Ghost
from modules.vision import Vision

# Initialize Colors
init(autoreset=True)

def banner():
    print(Fore.RED + """
  _   _                      _ __  __ _           _ 
 | \ | | ___ _   _ _ __ __ _| |  \/  (_)_ __   __| |
 |  \| |/ _ \ | | | '__/ _` | | |\/| | | '_ \ / _` |
 | |\  |  __/ |_| | | | (_| | | |  | | | | | | (_| |
 |_| \_|\___|\__,_|_|  \__,_|_|_|  |_|_|_| |_|\__,_|
      """ + Fore.WHITE + "v1.0.0 // AI POWERED SECURITY CORE"
      " BY https://github.com/devnand-47")

def main_menu():
    banner()
    print("\n[1] 🧠 Cortex (Code Vulnerability Scan)")
    print("[2] 👻 Ghost  (Steganography / Hide Text)")
    print("[3] 👁️ Vision (Network Recon)")
    print("[0] Exit")
    
    choice = input(f"\n{Fore.RED}root@neuralmind:~#{Style.RESET_ALL} ")
    
    if choice == '1':
        target = input("Enter filename to scan (e.g. main.py): ")
        Cortex().scan_code(target)
    
    elif choice == '2':
        mode = input(" (E)ncrypt or (D)ecrypt? ").upper()
        img = input("Enter image filename (e.g. photo.png): ")
        if mode == 'E':
            msg = input("Enter secret message: ")
            Ghost().hide_data(img, msg)
        else:
            Ghost().reveal_data(img)
            
    elif choice == '3':
        ip = input("Enter Target IP (e.g. 192.168.1.1): ")
        Vision().scan_network(ip)
        
    elif choice == '0':
        sys.exit()
    else:
        print("Invalid option.")

if __name__ == "__main__":
    while True:
        main_menu()