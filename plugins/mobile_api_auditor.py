import sys
import requests

def audit_mobile_api(target):
    print(f"[📱] Auditing Mobile-Specific API Endpoints for {target}...")
    mobile_paths = ["/api/v1/mobile/login", "/api/v1/device/register", "/api/v1/app/config"]
    
    findings = []
    for path in mobile_paths:
        try:
            r = requests.get(f"http://{target}{path}", headers={"User-Agent": "Android-Mobile-App"}, timeout=5)
            if r.status_code == 200:
                findings.append(f"MOBILE_ENDPOINT_EXPOSED: {path}")
        except: continue
    return "\n".join(findings) if findings else "No mobile-specific leaks found."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(audit_mobile_api(sys.argv[1]))
