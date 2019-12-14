import requests
def Getinfo(url):
    r=requests.get(url)
    return r.text
