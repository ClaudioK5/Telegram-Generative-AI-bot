import requests
from AI_response_generator import AI_response_generator
from datetime import datetime
import time



while True:

    BOT_TOKEN = "insert here your telegram bot key"

    CHANNEL_ID = "insert here your own telegram channel"

    today = datetime.today()

    prompt = "write your prompt for everyday generation"

    message = AI_response_generator(prompt)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
    "chat_id": CHANNEL_ID,
    "text": message
    }

    response = requests.post(url, data=payload)

    print(response.json())

    time.sleep(86400)
