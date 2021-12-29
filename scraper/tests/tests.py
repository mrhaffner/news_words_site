from django.test import TestCase
from django.core.exceptions import ValidationError
from scraper.models import RSS_Page
from scraper.scraper import Scraper


class ScraperTest(TestCase):

    def get_mock_page(self) -> str:
        with open('scraper/tests/mock_rss.html') as file:
            html = file.read()
        return html

    
    def get_mock_url(self) -> str:
        return 'http://rss.cnn.com/rss/cnn_topstories.rss'

    
    def test_scraper_saves_raw_rss_page(self) -> None:
        mock_page, mock_url = self.get_mock_page(), self.get_mock_url()
        Scraper.save_rss_page(mock_page, mock_url)
        self.assertEqual(RSS_Page.objects.count(), 1)


    def test_cannot_save_rss_page_with_empty_html(self) -> None:
        rss_page = RSS_Page(html='')
        with self.assertRaises(ValidationError):
            rss_page.full_clean()
            rss_page.save()
        self.assertEqual(RSS_Page.objects.count(), 0)
        

    def test_scraper_cannot_save_rss_page_with_empty_fields(self) -> None:
        mock_page, mock_url = self.get_mock_page(), self.get_mock_url()
        Scraper.save_rss_page('', mock_url)
        Scraper.save_rss_page(mock_page, '')
        self.assertEqual(RSS_Page.objects.count(), 0)

    
    def test_scraper_retries_after_receiving_empty_html(self) -> None:
        self.fail()