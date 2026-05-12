import sys, requests, json, socket

def get_intel(target):
    print(f"[*] Extracting Intelligence for: {target}")
    try:
        ip = socket.gethostbyname(target)
        # Real Shodan API Call (Add your key here)
        # API_KEY = "YOUR_SHODAN_KEY"
        # r = requests.get(f"https://api.shodan.io/shodan/host/{ip}?key={API_KEY}")
        
        # DNS & Banner Grabbing Logic
        tech_data = {
            "target": target,
            "ip": ip,
            "dns_records": socket.gethostbyname_ex(target),
            "osint_summary": "Active Infrastructure Detected"
        }
        return json.dumps(tech_data, indent=4)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(get_intel(sys.argv[1]))
