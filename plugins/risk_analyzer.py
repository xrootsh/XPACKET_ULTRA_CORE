import sys
import json

def calculate_risk(mission_data):
    score = 0
    findings = mission_data.lower()
    
    # Risk Logic
    if "waf detected" in findings: score += 10
    if "critical" in findings: score += 40
    if "vulnerability found" in findings: score += 30
    if "shell_access_granted" in findings: score += 20
    
    status = "LOW"
    if score > 70: status = "CRITICAL"
    elif score > 40: status = "MEDIUM"
    
    result = {
        "risk_score": score,
        "threat_level": status,
        "recommendation": "Escalate to Aggressive Strike" if score > 50 else "Continue Recon"
    }
    return json.dumps(result, indent=4)

if __name__ == "__main__":
    # In a real scenario, this would read the DB or JSON files
    if len(sys.argv) > 1:
        print(calculate_risk(sys.argv[1]))
