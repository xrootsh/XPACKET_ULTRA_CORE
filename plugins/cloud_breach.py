import sys
import requests

def cloud_audit(target):
    print(f"[!] Target {target}: Initiating Cloud Infrastructure Audit...")
    # Common Cloud Metadata & Bucket Patterns
    cloud_vectors = [
        f"http://s3.amazonaws.com/{target}",
        f"http://{target}.s3.amazonaws.com",
        "http://169.254.169.254/latest/meta-data/" # SSRF / Metadata check
    ]
    
    findings = []
    for url in cloud_vectors:
        try:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                findings.append(f"EXPOSED CLOUD ASSET: {url}")
        except: continue
        
    return "\n".join(findings) if findings else "No public cloud exposures found."

if __name__ == "__main__":
    if len(sys.argv) > 1: print(cloud_audit(sys.argv[1]))
