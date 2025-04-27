import requests
from bs4 import BeautifulSoup

base_url = 'http://localhost:8080'

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', href=True)

# API linklerini filtrele
api_links = [link['href'] for link in links if '/api/' in link['href']]
print('Bulunan API Linkleri:')
for api_link in api_links:
    print(f'{base_url}{api_link}')
