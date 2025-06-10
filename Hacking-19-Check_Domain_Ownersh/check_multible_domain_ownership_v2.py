import whois

def check_domains(domains):
    results = {}
    for domain in domains:
        try:
            w = whois.whois(domain)
            if w.domain_name:
                results[domain] = "Kayıtlı"
            else:
                results[domain] = "Boşta"
        except Exception as e:
            results[domain] = f"HATA: {str(e)}"
    return results

# 🔍 Kontrol edilecek domain listesi
domain_list = [
    "google.com",
    "openai.com",
    "somefakenewdomain123456.com",  # büyük ihtimalle boşta
    "celalaygar.com"
]

# ✅ Domainleri kontrol et
sonuclar = check_domains(domain_list)

# 🖨️ Sonuçları yazdır
for domain, durum in sonuclar.items():
    print(f"{domain}: {durum}")
