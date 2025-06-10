# install library
#
# pip install python-whois
#

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
        except Exception:
            results[domain] = "Boşta veya erişim hatası"
    return results

domain_list = [
    "google.com",
    "openai.com",
    "celalaygarx.com",  # büyük ihtimalle boşta
    "celalaygar.com"
]

sonuclar = check_domains(domain_list)

for domain, durum in sonuclar.items():
    print(f"{domain}: {durum}")
