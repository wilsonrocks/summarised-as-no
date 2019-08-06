import requests
from bs4 import BeautifulSoup
from pprint import pprint

html = requests.get('https://bbc.co.uk/news').content
parsed = BeautifulSoup(html, features='lxml')

for match in parsed.find_all():
    if match.name != 'a':
        match.replaceWithChildren()

all_links = parsed.find_all('a')


question_links = ([link for link in all_links if link.text.endswith('?')])

for link in question_links:
    attrs = dict(link.attrs)
    for attr in attrs:
        if attr != 'href':
            del link.attrs[attr]


pprint(question_links)
