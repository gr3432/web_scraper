import requests
from bs4 import BeautifulSoup

url = "https://www.universityadmissions.se/intl/search?period=1&freeText=Japanese&semesterPart=0"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# Get search results and reduce unnecessary information
search_results = soup.find('ul', class_='searchResult').find_all('li')

search_results = [li.find_all('span', class_='appl_fontsmall') for li in search_results]

# the first span contains the credits and the second the university name and location
search_results = [uni[1].text.strip().lower() for uni in search_results]

assert [uni for uni in search_results if "dalarna" in uni] == []