from django.test import TestCase
from django.core.exceptions import ValidationError
from scraper.models import RSSPage
from scraper.scraper import Scraper


MOCK_WEBSITE_NAME = 'cnn'
MOCK_URL = 'http://rss.cnn.com/rss/cnn_topstories.rss'

class ScraperTest(TestCase):

    def get_mock_page(self) -> str:
        with open('scraper/tests/mock_rss.html') as file:
            html = file.read()
        return html

    
    def test_scraper_saves_raw_rss_page(self) -> None:
        mock_page = self.get_mock_page()
        Scraper.save_rss_page(mock_page, MOCK_URL, MOCK_WEBSITE_NAME)
        self.assertEqual(RSSPage.objects.count(), 1)
        

    def test_scraper_cannot_save_rss_page_with_empty_fields(self) -> None:
        mock_page = self.get_mock_page()
        Scraper.save_rss_page('', MOCK_URL, MOCK_WEBSITE_NAME)
        Scraper.save_rss_page(mock_page, '', MOCK_WEBSITE_NAME)
        Scraper.save_rss_page(mock_page, MOCK_URL, '')
        self.assertEqual(RSSPage.objects.count(), 0)

    
    def test_scraper_saves_list_of_rss_pages(self) -> None:
        self.fail()


    def test_scraper_retries_after_receiving_empty_html(self) -> None:
        self.fail()


class RSSPageTest(TestCase):

    def test_cannot_save_rss_page_with_empty_html(self) -> None:
        rss_page = RSSPage(html='', url=MOCK_URL, website_name=MOCK_WEBSITE_NAME)
        with self.assertRaises(ValidationError):
            rss_page.full_clean()
            rss_page.save()
        self.assertEqual(RSSPage.objects.count(), 0)