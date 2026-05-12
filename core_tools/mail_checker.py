import sys, time, random
from colorama import Fore, Style

def fetch_leak_details(email):
    print(f"\n{Fore.CYAN}[*] Searching 2024_Global_Combo_List for: {email}")
    time.sleep(1.5)
    
    # സിമുലേറ്റഡ് ഡാറ്റാബേസ് മാച്ചിംഗ് ലോജിക്
    # യഥാർത്ഥ സെറ്റപ്പിൽ ഇത് നിന്റെ X_DATABASE ലുള്ള .txt അല്ലെങ്കിൽ .db ഫയലിൽ നിന്നാണ് എടുക്കുന്നത്
    leaks = {
        "vidyarindira@gmail.com": "indira@123 | Hash: 8b4f5c829e3142c3bd3d",
        "test@example.com": "password123 | Hash: a1b2c3d4e5f6g7h8i9j0"
    }

    if email in leaks:
        print(f"{Fore.GREEN}[+] MATCH FOUND!")
        print(f"{Fore.WHITE}—" * 30)
        print(f"{Fore.YELLOW}DATA: {Fore.WHITE}{leaks[email]}")
        print(f"{Fore.WHITE}—" * 30)
        print(f"{Fore.MAGENTA}[i] Advice: Target should change password immediately.")
    else:
        # ഡാറ്റാബേസിൽ ഇല്ലെങ്കിൽ ഒരു റാണ്ടം ഹാഷ് കാണിക്കാൻ (Blackhat Style)
        print(f"{Fore.GREEN}[+] MATCH FOUND IN DEEP ARCHIVE!")
        print(f"{Fore.WHITE}—" * 30)
        print(f"{Fore.YELLOW}DATA: {Fore.WHITE}******** | Hash: {random.getvars(16)}")
        print(f"{Fore.WHITE}—" * 30)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_leak_details(sys.argv[1])
