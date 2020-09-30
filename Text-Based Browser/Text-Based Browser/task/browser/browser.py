import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore


# write your code here
def open_page(location, url):
    r = requests.get('http://' + url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li'])
    content = []
    for tag in tags:
        tag_text = tag.text.replace('\n', '')
        content.append(tag_text)
        if tag.name == 'a':
            print(Fore.BLUE + tag_text)
        else:
            print(Fore.BLACK + tag_text)
    file = url[0:url.rindex('.')]
    with open(location + '/' + file, 'w') as f:
        f.write('\n'.join(content))


def open_saved_page(location, url):
    file = url[0:url.rindex('.')]
    with open(location + '/' + file) as f:
        print(f.read())


dir_location = sys.argv[1]
prev_pages = []
if not os.path.exists(dir_location):
    os.makedirs(dir_location)
while True:
    url_address = input()
    if url_address == 'back':
        if len(prev_pages) > 1:
            open_saved_page(dir_location, prev_pages[len(prev_pages) - 2])
    elif url_address == 'exit':
        break
    elif '.' in url_address:
        prev_pages.append(url_address)
        open_page(dir_location, url_address)
    else:
        print('Sorry but you make error in url address')
