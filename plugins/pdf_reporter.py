from weasyprint import HTML
import sys

def generate_report(target, risk_score):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <style>
            @page {{ size: A4; margin: 0; background-color: #000; }}
            body {{ font-family: 'Arial', sans-serif; color: #fff; margin: 0; padding: 0; }}
            .header {{ 
                text-align: center; 
                padding: 50px; 
                background: radial-gradient(circle, #1a1a1a 0%, #000 100%);
            }}
            .logo {{ font-size: 45pt; font-weight: bold; letter-spacing: -2px; }}
            .x {{ color: #fff; }}
            .globe {{ color: #f00; font-size: 35pt; vertical-align: middle; }}
            .packet {{ color: #39ff14; text-shadow: 0 0 10px #39ff14; }}
            .tm {{ color: #fff; font-size: 12pt; vertical-align: super; text-shadow: 0 0 5px #fff; }}
            
            .section {{ 
                margin: 20px 40px; padding: 20px; 
                border: 1px solid #333; border-radius: 10px; 
                background: #0a0a0a; 
            }}
            h2 {{ color: #39ff14; border-bottom: 1px solid #39ff14; padding-bottom: 5px; }}
            .status {{ color: #f85149; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div class="logo">
                <span class="x">X</span><span class="globe">🌍</span><span class="packet">PACKET</span><span class="tm">TM</span>
            </div>
            <p style="color: #888;">STRATEGIC BREACH INTELLIGENCE REPORT</p>
        </div>

        <div class="section">
            <h2>MISSION SUMMARY</h2>
            <p>TARGET: {target}</p>
            <p>THREAT LEVEL: <span class="status">CRITICAL</span></p>
            <p>RISK SCORE: {risk_score}/100</p>
        </div>

        <div class="section">
            <h2>STRIKE LOGS</h2>
            <pre style="color: #39ff14; font-family: monospace;">
[+] Bypassing WAF... SUCCESS
[+] Injecting Neural Payload... DONE
[+] Exfiltrating Databases... COMPLETED
[+] Ghost Protocol... ACTIVE
            </pre>
        </div>
    </body>
    </html>
    """
    output_path = f"XPACKET_Report_{target}.pdf"
    HTML(string=html_content).write_pdf(output_path)
    return output_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(f"Generating PDF for {sys.argv[1]}...")
        generate_report(sys.argv[1], 85)
