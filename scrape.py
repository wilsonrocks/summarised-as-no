import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin

start_words = [
    'has',
    'have',
    'will',
    'are',
    'were',
    'is',
    'did',
]

output = []

with open('./sites') as sites:
    for site in sites:
        print(f'scraping {site}')

        html = requests.get('https://bbc.co.uk/news').content
        parsed = BeautifulSoup(html, features='lxml')

        for match in parsed.find_all():
            if match.name != 'a':
                match.replaceWithChildren()

        all_links = parsed.find_all('a')
        question_links = [
            link for link in all_links if (
                link.text.endswith('?')
            )
        ]

        for link in question_links:
            output.append({
                'url': urljoin(site.strip(), link['href']),
                'title': link.string,
            })


pprint(output)
