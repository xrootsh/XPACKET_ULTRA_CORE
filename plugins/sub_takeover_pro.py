import sys, socket

def check_takeover(target):
    print(f"[🔍] Checking for Subdomain Takeover on {target}...")
    services = ["github.io", "herokuapp.com", "cloudfront.net", "s3.amazonaws.com"]
    try:
        cname = socket.gethostbyname_ex(target)
        for s in services:
            if s in str(cname):
                return f"⚠️ POTENTIAL TAKEOVER: {target} is pointing to {s}"
    except: pass
    return "Subdomain seems secure."

if __name__ == "__main__":
    if len(sys.argv) > 1: print(check_takeover(sys.argv[1]))
