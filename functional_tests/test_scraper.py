import unittest
from bs4 import BeautifulSoup


class ScraperTest(unittest.TestCase):

    def setUp(self) -> None:
        html = None
        with open('functional_tests/mock_rss.html') as file:
            html = file.read()

        self.rss_feed = BeautifulSoup(html, 'html.parser')