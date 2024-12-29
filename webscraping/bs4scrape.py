from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-46435'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())
#print(soup.find_all('h1'))

box = soup.find('article', class_='main-article')

#title = soup.find('h1')
transcript = soup.find('div', class_='full-script').get_text()
print(transcript)
#print(box)
#print(box.prettify())
