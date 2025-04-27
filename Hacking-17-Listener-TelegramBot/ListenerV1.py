import requests
import time

BOT_TOKEN = 'TELEGRAM_BOT_TOKENIN'
CHAT_ID = 'KENDI_CHAT_IDN'  # Telefonundaki Telegram ID

def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()

def main():
    last_update_id = None
    
    while True:
        updates = get_updates(last_update_id)
        for update in updates.get("result", []):
            last_update_id = update["update_id"] + 1
            
            if "location" in update["message"]:
                latitude = update["message"]["location"]["latitude"]
                longitude = update["message"]["location"]["longitude"]
                print(f"Telefonun konumu: {latitude}, {longitude}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
