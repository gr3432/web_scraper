import requests
from bs4 import BeautifulSoup

url = 'https://sajp.info/applicationansokan/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

article = soup.find('article')

previous_content = '\n\nApplication/Ansökan \n\nOnline application for JLPT Stockhlm in July 2019 will be open March 1, 2019. Please read through the test guide 2019A below and have it at hand when you apply for the text.\n\ntest_guide_2019A\n\xa0\nWebbanmälan för JLPT Stockholm i Juli 2019 öppnar 1 mars, 2019 . Vänligen läs genom test guide 2019 nedan och ha det till hands när du anmäla dig till provet.\n\ntest_guide_2019A\nTest fee information\nLevel\xa0 Fee\nN1\xa0\xa0\xa0\xa0\xa0 SEK 500\nN2 \xa0 \xa0\xa0 SEK 500\nN3\xa0\xa0\xa0\xa0\xa0 SEK 400\nN4 \xa0 \xa0\xa0 SEK 300\nN5 \xa0 \xa0\xa0 SEK 300\nDela det här:TwitterFacebookGoogleGillaGilla Laddar... \n'

assert article.text == previous_content