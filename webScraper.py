from bs4 import BeautifulSoup
import requests
import pprint

resp = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(resp.text, 'html.parser')

content = soup.select('.storylink')
votes = soup.select('.subtext')

result = []
for index, item in enumerate(content):
    text = item.getText()
    href = item.get('href', None)
    points = votes[index].select('.score')
    if len(points):
        point = int(points[0].getText().replace(' points', ''))
        if point > 50:
            result.append({'text': text, 'href': href, 'point': point})

pprint.pprint(sorted(result, key=lambda k: k['point'], reverse=True))
