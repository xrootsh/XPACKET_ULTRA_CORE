#!/usr/bin/env python3
import os, subprocess
from colorama import Fore

class POCHarvester:
    def __init__(self):
        self.poc_store = "missions/pocs"
        os.makedirs(self.poc_store, exist_ok=True)

    def download_poc(self, cve_id, url):
        if not url or "search?q=" in url:
            return None

        # ഫോൾഡർ നെയിം ഉണ്ടാക്കുന്നു
        folder_name = cve_id.replace("/", "_").replace(" ", "_")
        target_dir = os.path.abspath(os.path.join(self.poc_store, folder_name))
        
        if os.path.exists(target_dir):
            subprocess.run(["rm", "-rf", target_dir])

        try:
            print(f"\n{Fore.CYAN}[*] Harvesting PoC for: {cve_id}")
            subprocess.run(["git", "clone", "--depth", "1", url, target_dir], check=True, capture_output=True)
            print(f"{Fore.GREEN}[✓] Success: PoC harvested to {target_dir}")
            return target_dir  # ഇപ്പോൾ ഇത് ശരിയായ പാത്ത് തിരിച്ചു നൽകും
        except Exception as e:
            print(f"{Fore.RED}[!] Harvest failed: {e}")
            return None
