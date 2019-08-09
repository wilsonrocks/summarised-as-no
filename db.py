import sqlite3

DATABASE_FILE = './articles.db'

connection = sqlite3.connect('articles.db')
cursor = connection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS article (url TEXT);')
connection.commit()


def site_visited(url):
    results = cursor.execute('SELECT * FROM article WHERE url=?;', (url,))
    return len(list(results)) > 0


def check_and_add_site(url):
    if site_visited(url):
        return False
    else:
        cursor.execute('INSERT INTO article VALUES (?);', (url,))
        connection.commit()
        return True
