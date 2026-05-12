import sys
import requests
import re

def discover(target):
    print(f"[*] Extracting Subdomains for: {target}")
    subdomains = set()
    url = f"https://crt.sh/?q=%25.{target}&output=json"
    try:
        response = requests.get(url, timeout=20)
        if response.status_code == 200:
            data = response.json()
            for entry in data:
                name = entry['name_value']
                for sub in name.split("\n"):
                    subdomains.add(sub.strip())
            return "\n".join(list(subdomains))
        return "No subdomains found."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(discover(sys.argv[1]))
