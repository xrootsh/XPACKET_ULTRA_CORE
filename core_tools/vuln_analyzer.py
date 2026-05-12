import subprocess, requests, json, os

class VulnAnalyzer:
    def __init__(self, neo4j_driver=None):
        self.driver = neo4j_driver

    def fetch_cves(self, product):
        print(f"  [?] Deep Probing Global Intelligence: {product}...")
        results = []
        
        # 1. CIRCL API (Aggressive Mode)
        try:
            # പക്കാ മാച്ചിംഗിന് പകരം കീവേഡ് സെർച്ച്
            clean_term = product.split()[0]
            r = requests.get(f"https://cve.circl.lu/api/search/{clean_term}", timeout=10)
            if r.status_code == 200 and r.json():
                print(f"  [+] Cloud: Fetched data from CIRCL.")
                results += [{"cve": i.get("id"), "cvss": i.get("cvss", 7.0), "summary": i.get("summary")} for i in r.json()[:10]]
        except: pass

        # 2. Local Arsenal (Termux Searchsploit Force)
        if not results:
            print(f"  [!] Cloud silent. Forcing Local Searchsploit...")
            try:
                # Termux-ൽ searchsploit കൃത്യമായി വിളിക്കുന്നു
                term = product.split()[0]
                cmd = ["searchsploit", term, "--json"]
                output = subprocess.check_output(cmd, text=True)
                data = json.loads(output)
                local_res = data.get("Results", [])
                if local_res:
                    print(f"  [+] Local: Found {len(local_res)} exploits in offline DB.")
                    results += [{"cve": i.get("Title")[:20], "cvss": 8.0, "summary": i.get("Title")} for i in local_res[:10]]
            except Exception as e:
                print(f"  [!] Local search failed: {e}")

        # 3. Emergency Fallback (Known High-Risk Mapping)
        if not results:
            print(f"  [!] No direct matches. Using Heuristic Mapping...")
            if "apache" in product.lower():
                results.append({"cve": "GENERIC-APACHE-RCE", "cvss": 9.8, "summary": "Multiple RCE and Path Traversal vulnerabilities in legacy Apache."})
            if "ssh" in product.lower():
                results.append({"cve": "GENERIC-SSH-AUTH", "cvss": 8.5, "summary": "Potential authentication bypass or user enumeration in OpenSSH."})

        return results

    def analyze(self, ip, services):
        print(f"\n[*] XPACKET ULTRA: Initiating Strike Analysis...")
        report = []
        for srv in services:
            vulns = self.fetch_cves(srv)
            for v in vulns:
                risk = float(v.get('cvss', 7.0)) * 10
                report.append({"service": srv, "vuln": v, "risk": risk})
        return report
