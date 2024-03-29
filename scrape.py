import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin, urlparse
from mailer import send_mail
from db import check_and_add_site

start_words = [
    'does',
    'has',
    'have',
    'will',
    'are',
    'was',
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
    return first_word in start_words and '?' in text


def collapse_links(soup):
    for match in soup.find_all():
        if match.name != 'a':
            match.replaceWithChildren()


errors = []

output = 'Howdy,\n'
sendAnything = False

with open('./sites') as sites:
    for site in [site.strip() for site in sites]:
        if site != '':
            print(f'scraping {site}')
            try:
                html = requests.get(site).content
                parsed = BeautifulSoup(html, features='lxml')
                collapse_links(parsed)
                all_links = parsed.find_all('a')

                question_links = [
                    link for link in all_links if is_question(link.text)]

                for link in question_links:
                    url_object = urlparse(urljoin(site.strip(), link['href']))
                    url = f'https://{url_object.netloc}{url_object.path}'
                    if check_and_add_site(url):
                        print(f'found: {link.string}')
                        print(url)
                        sendAnything = True
                        output += f'{link.string}\n {url}\n\n'
            except KeyboardInterrupt:
                exit(0)

            except Exception as e:
                print(f'error scraping{site}')
                print(e)


print('logging in and sending email')

send_mail(output if sendAnything else 'Howdy, no stories this time')
