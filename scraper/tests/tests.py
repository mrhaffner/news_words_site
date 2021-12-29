from django.test import TestCase
from bs4 import BeautifulSoup
from scraper.scraper import Scraper
from scraper.models import RSS_Post


class ScraperTest(TestCase):

    def get_mock_page(self) -> None:
        with open('scraper/tests/mock_rss.html') as file:
            html = file.read()
        return html

        # rss_feed = BeautifulSoup(html, 'html.parser')
        # return rss_feed

    
    def test_scraper_saves_rss_post(self) -> None:
        mock_page = self.get_mock_page()
        Scraper.save_rss_post(mock_page)
        #add more logic for fields?
        self.assertEqual(RSS_Post.objects.count(), 1)