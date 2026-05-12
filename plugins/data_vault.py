import sys
from cryptography.fernet import Fernet

def encrypt_data(data):
    key = Fernet.generate_key() # In production, save this key securely
    f = Fernet(key)
    encrypted = f.encrypt(data.encode())
    return f"KEY: {key.decode()}\nDATA: {encrypted.decode()}"

if __name__ == "__main__":
    if len(sys.argv) > 1: print(encrypt_data(sys.argv[1]))
