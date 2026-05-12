import os
import re

class PayloadConfigurer:
    @staticmethod
    def auto_configure(file_path, target_ip):
        """
        സ്ക്രിപ്റ്റിലെ RHOST, IP, TARGET പോലുള്ള വരികൾ കണ്ടെത്തി 
        ടാർഗെറ്റ് ഐപി വെച്ച് റീപ്ലേസ് ചെയ്യുന്നു.
        """
        if not os.path.exists(file_path): return False
        
        print(f"  [*] Auto-Configuring Payload: {file_path}")
        
        with open(file_path, 'r') as f:
            content = f.read()

        # പ്രിയോറിറ്റി ഉള്ള കീവേഡുകൾ
        patterns = {
            r'RHOST\s*=\s*["\'].*?["\']': f'RHOST = "{target_ip}"',
            r'target_ip\s*=\s*["\'].*?["\']': f'target_ip = "{target_ip}"',
            r'ip_address\s*=\s*["\'].*?["\']': f'ip_address = "{target_ip}"'
        }

        new_content = content
        for pattern, replacement in patterns.items():
            new_content = re.sub(pattern, replacement, new_content, flags=re.IGNORECASE)

        with open(file_path, 'w') as f:
            f.write(new_content)
            
        print(f"  [✓] Payload Arming Complete for {target_ip}")
        return True
