import whois # pip install python-whois


# reference link : https://www.thepythoncode.com/article/extracting-domain-name-information-in-python

def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)
      
      
domains = [
    "thepythoncode.com",
    "google.com",
    "github.com",
    "unknownrandomdomain.com",
    "notregistered.co"
]
# iterate over domains
for domain in domains:
    print(domain, "is registered" if is_registered(domain) else "is not registered")
      
      
      
      
