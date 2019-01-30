import requests
from bs4 import BeautifulSoup

url = 'https://sajp.info/applicationansokan/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

article = soup.find('article')

previous_content = '\n\nApplication/Ansökan \n\n\xa0\nOnline application for JLPT Stockhlm in July 2019 will be open March 1, 2019.\n\n\xa0\nWebbanmälan för JLPT Stockholm i Juli 2019 öppnar 1 mars, 2019 .\n.\n\xa0\n\xa0\nDela det här:TwitterFacebookGoogleGillaGilla Laddar... \n'

assert article.text == previous_content