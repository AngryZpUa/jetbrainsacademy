import requests

from bs4 import BeautifulSoup


title_index = int(input())
url_address = input()
r = requests.get(url_address)
soup = BeautifulSoup(r.content, 'html.parser')
h2s = soup.find_all('h2')
i = 0
for h2 in h2s:
    if i == title_index:
        print(h2.text)
        break
    else:
        i += 1
