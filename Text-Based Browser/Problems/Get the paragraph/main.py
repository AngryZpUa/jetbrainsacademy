import requests

from bs4 import BeautifulSoup

word = input()
url_address = input()
r = requests.get(url_address)
soup = BeautifulSoup(r.content, 'html.parser')
ps = soup.find_all('p')
for p in ps:
    if word in p.text:
        print(p.text)
        break
