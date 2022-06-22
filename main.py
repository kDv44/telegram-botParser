import requests
from bs4 import BeautifulSoup as b


URL = 'https://www.autocentre.ua/avtosport'
req = requests.get(URL)
soup = b(req.text, 'html.parser')

title_news = soup.find_all('div', class_='title')
link_news = soup.find_all('div', class_='item')

print(f"{title_news}\n{link_news}")
