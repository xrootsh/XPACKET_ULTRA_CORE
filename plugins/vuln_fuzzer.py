import sys, requests

PATHS = ["/.env", "/.git/config", "/admin/config.php", "/wp-config.php.bak", "/config.json"]

def start_fuzzing(target):
    print(f"[!] Fuzzing Sensitive Endpoints on {target}...")
    found = []
    for path in PATHS:
        try:
            url = f"http://{target}{path}"
            r = requests.get(url, timeout=5)
            if r.status_code == 200 and len(r.text) > 0:
                found.append(f"VULNERABILITY FOUND: {path}")
        except:
            continue
    return "\n".join(found) if found else "No critical exposures identified."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(start_fuzzing(sys.argv[1]))
