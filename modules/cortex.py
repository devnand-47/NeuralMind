import re
from colorama import Fore, Style

class Cortex:
    def scan_code(self, file_path):
        print(f"\n[{Fore.CYAN}*{Style.RESET_ALL}] Cortex AI analyzing: {file_path}...")
        
        # Simple "AI" patterns to look for
        patterns = {
            "Hardcoded Password": r"password\s*=\s*['\"]",
            "Dangerous Exec": r"exec\(",
            "SQL Injection Risk": r"SELECT .* FROM .* \+ .*",
            "IP Address Leak": r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        }
        
        try:
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()
                
            issues_found = 0
            for risk, regex in patterns.items():
                if re.search(regex, content, re.IGNORECASE):
                    print(f"[{Fore.RED}!{Style.RESET_ALL}] ALERT: {risk} detected.")
                    issues_found += 1
            
            if issues_found == 0:
                print(f"[{Fore.GREEN}✓{Style.RESET_ALL}] Code looks clean.")
            else:
                print(f"\n[{Fore.RED}X{Style.RESET_ALL}] Scan complete. {issues_found} potential risks found.")
                
        except FileNotFoundError:
            print(f"[{Fore.YELLOW}?{Style.RESET_ALL}] Error: File not found.")