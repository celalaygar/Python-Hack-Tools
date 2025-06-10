# install library
#
# pip install python-whois
#

import whois

# Sessiz harfler (Türkçe karakterler hariç, İngilizce alfabeye göre)
consonants = "bcdfghjklmnpqrstvwxyz"

# Domain listesini oluştur (örneğin: boogy.com, coogy.com, ..., zoogy.com)
domains = [f"{letter}oogy.com" for letter in consonants]

def check_domain_ownership(domains):
    results = {}
    for domain in domains:
        try:
            w = whois.whois(domain)
            if w.domain_name:
                results[domain] = "Kayıtlı"
            else:
                results[domain] = "Boşta"
        except Exception:
            # WHOIS hatası alınırsa genelde bu domain kayıtlı değildir.
            results[domain] = "Boşta veya erişim hatası"
    return results

# Domainleri kontrol et
results = check_domain_ownership(domains)

# Sonuçları yazdır
for domain, status in results.items():
    print(f"{domain}: {status}")
