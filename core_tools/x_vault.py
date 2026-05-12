import os

def show_vault():
    print("\n" + "="*30)
    print(" 🔐 X🔴PACKET™ SECURE VAULT")
    print("="*30)
    files = [f for f in os.listdir('.') if f.endswith('.json') or f.endswith('.csv')]
    if not files:
        print("[!] Vault is empty. No reports found.")
    else:
        for i, f in enumerate(files, 1):
            print(f" [{i}] {f}")
    print("\n[#] Press Enter to return...")

if __name__ == "__main__":
    show_vault()
