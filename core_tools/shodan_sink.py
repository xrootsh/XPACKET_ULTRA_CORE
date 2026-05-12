import shodan
from colorama import Fore

class ShodanSink:
    def __init__(self, api_key):
        self.api = shodan.Shodan(api_key)

    def find_targets(self, query, limit=10):
        print(f"{Fore.CYAN}[*] Querying Shodan Intelligence for: {query}")
        try:
            results = self.api.search(query)
            ips = [{"ip": r['ip_str'], "port": r['port'], "org": r.get('org', 'Unknown')} for r in results['matches'][:limit]]
            print(f"{Fore.GREEN}[+] Found {len(ips)} live targets on the internet.")
            return ips
        except Exception as e:
            print(f"{Fore.RED}[!] Shodan API Error: {e}")
            return []
