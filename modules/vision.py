import socket
import threading
from colorama import Fore, Style

class Vision:
    def scan_network(self, target_ip):
        print(f"\n[{Fore.CYAN}*{Style.RESET_ALL}] Vision Active. Scanning {target_ip}/24 subnet...")
        
        # Determine the base IP (e.g., 192.168.1.)
        base_ip = ".".join(target_ip.split('.')[:-1]) + "."
        
        def check_port(ip):
            try:
                # We check port 135 (common Windows port) just to see if host is up
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, 135))
                if result == 0:
                    print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Host Up: {ip}")
                sock.close()
            except:
                pass

        # Scan 1 to 50 (Keep it small for speed/demo)
        threads = []
        for i in range(1, 51):
            ip = base_ip + str(i)
            t = threading.Thread(target=check_port, args=(ip,))
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()
            
        print(f"[{Fore.CYAN}*{Style.RESET_ALL}] Scan Complete.")