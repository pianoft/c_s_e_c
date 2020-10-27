import codecs
from bs4 import BeautifulSoup
import requests
import bs4

baseUrl = "https://ksnctf.sweetduet.info/problem/2"

response = requests.get(baseUrl)

soup = bs4.BeautifulSoup(response.text, 'html.parser')

texts = soup.find('div', {'class': 'well'}).find(text=True, recursive=False)


def rot13(s):
    return codecs.encode(s, 'rot-13')

print(rot13(texts))
