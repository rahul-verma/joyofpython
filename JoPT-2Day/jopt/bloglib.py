import requests


def get_author_data(start, end):
    url = 'https://jsonplaceholder.typicode.com/users'
    authors = requests.get(url).json()[start:end]
    for author in authors:
        del author['address']
        del author['company']
    return authors
