import requests
from bs4 import BeautifulSoup

url = 'https://sajp.info/applicationansokan/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

article = soup.find('article')

print(article.text)
