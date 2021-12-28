from django.test import TestCase
from bs4 import BeautifulSoup


class ScraperTest(TestCase):

    def get_mock_page(self) -> None:
        with open('scraper/tests/mock_rss.html') as file:
            html = file.read()

        rss_feed = BeautifulSoup(html, 'html.parser')
        return rss_feed

