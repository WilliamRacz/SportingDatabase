import requests

def send_request(url):
    resp = requests.get(url)
    resp.raise_for_status()
    return resp