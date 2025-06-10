import whois

def get_domain_info(domain):
    try:
        w = whois.whois(domain)
        if w.domain_name:
            return {
                "Durum": "Kayıtlı",
                "Domain": domain,
                "Registrar": w.registrar,
                "Oluşturulma Tarihi": w.creation_date,
                "Bitiş Tarihi": w.expiration_date,
                "Güncellenme Tarihi": w.updated_date,
                "Name Servers": w.name_servers,
                "E-posta": w.emails,
            }
        else:
            return {"Durum": "Boşta", "Domain": domain}
    except Exception as e:
#           return {"Durum": f"HATA: {str(e)}", "Domain": domain}
            return {"Durum": "Boşta veya erişim hatası", "Domain": domain}

# 🔍 Kontrol edilecek domain listesi
domain_list = [
    "google.com",
    "openai.com",
    "celalaygar.com",
    "somefakenewdomain123456.com"
]

# 🧾 Sonuçları al
for domain in domain_list:
    info = get_domain_info(domain)
    print("\n" + "="*50)
    for key, value in info.items():
        print(f"{key}: {value}")
