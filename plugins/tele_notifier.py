import sys
import requests

def send_alert(message):
    token = "YOUR_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    try:
        requests.get(url)
        return "ALERT_SENT"
    except:
        return "FAILED_TO_SEND"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_alert(sys.argv[1])
