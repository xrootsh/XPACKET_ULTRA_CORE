import sys, random, requests

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
]

def bypass_check(target):
    header = {"User-Agent": random.choice(USER_AGENTS)}
    print(f"[*] Spoofing Identity as: {header['User-Agent']}")
    try:
        r = requests.get(f"http://{target}", headers=header, timeout=10)
        return f"Evasion Status: SUCCESS (Status Code: {r.status_code})"
    except:
        return "Evasion Status: FAILED"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(bypass_check(sys.argv[1]))
