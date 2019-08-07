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
    'could',
    'should',
    'would',
    'do'
]


def is_question(text):
    first_word = text.split(' ')[0].lower()
    return first_word in start_words


output = []

with open('./sites') as sites:
    for site in sites:
        print(f'scraping {site}')

        html = requests.get(site).content
        parsed = BeautifulSoup(html, features='lxml')

        for match in parsed.find_all():
            if match.name != 'a':
                match.replaceWithChildren()

        all_links = parsed.find_all('a')
        question_links = [
            link for link in all_links if (
                is_question(link.text) and '?' in link.text
            )
        ]

        for link in question_links:
            output.append({
                'url': urljoin(site.strip(), link['href']),
                'title': link.string,
            })


pprint(output)
