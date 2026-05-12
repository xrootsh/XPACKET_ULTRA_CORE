import sys
import requests

def detect_waf(target):
    print(f"[*] Analyzing WAF for: {target}")
    try:
        # Malicious looking request to trigger WAF
        url = f"http://{target}/?id=' OR 1=1--"
        response = requests.get(url, timeout=10)
        
        headers = response.headers
        server = headers.get("Server", "").lower()
        
        if "cloudflare" in server or "cf-ray" in headers:
            return "RESULT: WAF Detected [Cloudflare]"
        elif "akamai" in server:
            return "RESULT: WAF Detected [Akamai]"
        elif response.status_code == 403:
            return "RESULT: Possible WAF Block (Status 403)"
        
        return "RESULT: No obvious WAF detected."
    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(detect_waf(sys.argv[1]))
