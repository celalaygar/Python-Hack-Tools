from linkfinder import LinkFinder

# # # #
# instal python library on terminal
# pip install linkfinder
# # # #

base_url = 'http://localhost:8080'
response = requests.get(base_url)

finder = LinkFinder()
finder.feed(response.text)

# Tüm linkleri al
api_links = [link for link in finder.links if '/api/' in link]
print('Bulunan API Linkleri:')
for link in api_links:
    print(link)
