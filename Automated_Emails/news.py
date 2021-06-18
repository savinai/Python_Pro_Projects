# Api Key: get the key from newsapi.org
import requests
from pprint import pprint


class NewsFeed:
    """
    Representing multiple news titles and links as a single string
    """

    base_url = 'https://newsapi.org/v2/everything?'
    api_key = '' #get the key from newsapi.org

    def __init__(self, interest, from_date):
        self.interest = interest
        self.from_date = from_date

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f'{self.base_url}' \
              f'q={self.interest}&' \
              f'from={self.from_date}&' \
              f'sortBy=publishedAt&' \
              f'apiKey={self.api_key}'  
        return url

# Disposable email ids from dropmail.me


