import requests
from bs4 import BeautifulSoup

url = "https://www.universityadmissions.se/intl/search?period=1&freeText=Japanese&semesterPart=0"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

search_results = soup.find('ul', class_='searchResult').find_all('li')

