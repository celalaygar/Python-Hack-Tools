# install library
#
# pip install python-whois
#

import whois

def is_domain_registered(domain):
    try:
        w = whois.whois(domain)
        return bool(w.domain_name)
    except Exception:
        return False

# Örnek kullanım
domain = "coomy.com"  # Buraya kontrol etmek istediğiniz domaini yazın
if is_domain_registered(domain):
    print(f"{domain} kayıtlı (sahibi var).")
else:
    print(f"{domain} boşta (sahibi yok).")
