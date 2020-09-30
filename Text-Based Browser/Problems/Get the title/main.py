import requests

from bs4 import BeautifulSoup

r = requests.get(input())
soup = BeautifulSoup(r.content, 'html.parser')
h1s = soup.find_all('h1')
for h1 in h1s:
    print(h1.text)
