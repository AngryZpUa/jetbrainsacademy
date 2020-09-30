import requests


def check_success(url):
    r = requests.get(url)
    if r.ok:
        return 'Success'
    else:
        return 'Fail'
