from stegano import lsb
from colorama import Fore, Style
import os

class Ghost:
    def hide_data(self, image_path, secret_msg):
        print(f"\n[{Fore.CYAN}*{Style.RESET_ALL}] Encrypting data into image...")
        try:
            secret = lsb.hide(image_path, secret_msg)
            output_filename = "secret_image.png"
            secret.save(output_filename)
            print(f"[{Fore.GREEN}✓{Style.RESET_ALL}] Success! Data hidden in {output_filename}")
        except Exception as e:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] Error: {e}")

    def reveal_data(self, image_path):
        print(f"\n[{Fore.CYAN}*{Style.RESET_ALL}] Extracting data from image...")
        try:
            clear_message = lsb.reveal(image_path)
            print(f"[{Fore.GREEN}✓{Style.RESET_ALL}] DECODED MESSAGE: {Fore.YELLOW}{clear_message}{Style.RESET_ALL}")
        except:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] No hidden data found.")