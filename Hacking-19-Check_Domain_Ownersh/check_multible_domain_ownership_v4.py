import whois

def get_domain_info(domain):
    try:
        w = whois.whois(domain)
        if w.domain_name:
            return {
                "Durum": "Kayıtlı",
                "Domain": domain,
                "Registrar": w.registrar,
                # "Oluşturulma Tarihi": w.creation_date,
                # "Bitiş Tarihi": w.expiration_date,
                # "Güncellenme Tarihi": w.updated_date,
                # "Name Servers": w.name_servers,
                # "E-posta": w.emails,
            }
        else:
            return {"Durum": "Boşta", "Domain": domain}
    except Exception as e:
            return {"Durum": "Boşta veya erişim hatası", "Domain": domain}

# 🔍 Kontrol edilecek domain listesi
domain_list = [
    "knightai.com",
    "knifeai.com",
    "poonai.com",
    "poogyai.com",
    "toogleim.com",
    "lokumai.com",
    "bakai.com",
    "lookai.com",
    "lookupai.com",
    "lookatai.com",
    "watchai.com",
    "watchoutai.com",
    "matchai.com",
    "payforai.com",
    "forai.com",
    "foreachai.com",
    "loopai.com",
    "muckai.com",
    "kissai.com",
    "feai.com",
    "geai.com",
    "readai.com",
    "readerai.com",
    "writerai.com",
    "gagetai.com",
    "cableai.com",
    "wireai.com",
    "mineai.com",
    "meai.com",
    "thatai.com",
    "thisai.com"
]

# 🧾 Sonuçları al
for domain in domain_list:
    info = get_domain_info(domain)
    print("\n" + "="*50)
    for key, value in info.items():
        print(f"{key}: {value}")
