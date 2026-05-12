import sys
import requests

def api_strike(target):
    print(f"[!] Target {target}: Engaged API Lethal Mode...")
    endpoints = ["/api/v1/user/1", "/api/debug", "/v2/auth/config", "/swagger.json"]
    
    breaches = []
    for ep in endpoints:
        try:
            url = f"http://{target}{ep}"
            # Testing for BOLA / Unauthorized Access
            r = requests.get(url, timeout=5)
            if r.status_code == 200 and ("user" in r.text or "config" in r.text):
                breaches.append(f"CRITICAL API LEAK: {ep}")
        except: continue
        
    return "\n".join(breaches) if breaches else "API Endpoints Secured."

if __name__ == "__main__":
    if len(sys.argv) > 1: print(api_strike(sys.argv[1]))
