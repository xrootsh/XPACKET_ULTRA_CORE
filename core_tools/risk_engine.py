import random

class XPACKETRiskEngine:
    def __init__(self):
        # സിസ്റ്റം വിശകലനം ചെയ്യേണ്ട കീവേഡുകൾ
        self.critical_services = ['ssh', 'ftp', 'http', 'mysql', 'smb', 'rdp']

    def predict_risk(self, target, ports):
        # AI Logic Simulation: ഓപ്പൺ പോർട്ടുകളുടെ എണ്ണവും ടൈപ്പും നോക്കി സ്കോർ നൽകുന്നു
        base_score = len(ports) * 10
        if any(service in str(ports).lower() for service in self.critical_services):
            base_score += 30
        
        # 0 - 100 പരിധിയിൽ സ്കോർ സെറ്റ് ചെയ്യുന്നു
        final_score = min(base_score + random.randint(1, 10), 100)
        
        status = "LOW"
        if final_score > 70: status = "CRITICAL 🔥"
        elif final_score > 40: status = "MEDIUM ⚠️"
        
        return final_score, status

if __name__ == "__main__":
    engine = XPACKETRiskEngine()
    score, status = engine.predict_risk("103.21.244.x", [80, 443, 22])
    print(f"Risk Score: {score}% | Status: {status}")
