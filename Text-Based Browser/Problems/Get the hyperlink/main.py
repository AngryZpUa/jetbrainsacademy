import requests

from bs4 import BeautifulSoup


def parse_response(soup, act):
    a_s = soup.find_all('a')
    for a in a_s:
        if act in a.text:
            print(a.get('href'))
            return


number_of_act = input()
url_address = input()
r = requests.get(url_address)
parse_response(BeautifulSoup(r.content, 'html.parser'), number_of_act)
