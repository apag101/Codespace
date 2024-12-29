from bs4 import BeautifulSoup
import requests
import time

root = 'https://quotes.toscrape.com'
result = requests.get(root)
content = result.text
soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())
#print(soup.find_all('h1'))

# pagination = soup.find('li', class_='next')
# print(pagination)

# for next in range(1, int(pagination.text)+1):
#     website = f'{root}{link}'
#     result = requests.get(website)
#     content = result.text
#     soup = BeautifulSoup(content, 'html.parser')

box = soup.find('div', class_='container')
title = soup.find('title').get_text()


print(title)
links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])


for link in links:
    website = f'{root}{link}'
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')

    author = box.find(attrs={"class":"author"}).get_text()
    summary = box.find(attrs={"class":"quote"}).get_text()
    with open(f'{author}.txt', 'w') as file:
        file.write(f'{website} \n{summary} \n')
        file.close()
#print(website)

# transcript = soup.find('title').get_text(strip=True, separator=' ')
# print(transcript)
#print(title)
# #print(box)
# #print(box.prettify())

