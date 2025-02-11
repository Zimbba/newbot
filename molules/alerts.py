import requests

TELEGRAM_BOT_TOKEN = "SEU_BOT_TOKEN"
TELEGRAM_CHAT_ID = "SEU_CHAT_ID"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)
