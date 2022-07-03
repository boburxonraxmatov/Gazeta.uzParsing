import requests
import json
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Window/10'
}

rubrika = input('Введите рубрику: ')
html = requests.get(f'https://www.gazeta.uz/ru/{rubrika}/',headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
articles = soup.find_all('div',class_='nt')

json_data = []

for article in articles:
    data = article.find('div', class_='ndt').text
    title = article.find('h3').text
    teaser = article.find('p').text
    json_data.append({
        'title':title,
        'teaser':teaser,
        'data':data
    })
    print(json_data)

    with open('gazeta.json', mode='w', encoding='UTF-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)

