import json
from django.test import TestCase
from django.core.exceptions import ValidationError
from scraper.models import RSSPage
from scraper.scraper import Scraper
from unittest import mock


MOCK_WEBSITE_NAME = 'cnn'
MOCK_URL = 'http://rss.cnn.com/rss/cnn_topstories.rss'
with open('scraper/static/mock_rss.html') as file:
    MOCK_HTML = file.read()
# Move constants to just getting from json?

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, html_page, status_code):
            self.html_page = html_page
            self.status_code = status_code

        def html(self):
            return self.html_page

    if args[0] == MOCK_URL:
        yield MockResponse(MOCK_HTML, 200)

    yield MockResponse(None, 404)


class ScraperTest(TestCase):

    def get_mock_page(self) -> str:
        with open('scraper/static/mock_rss.html') as file:
            html = file.read()
        return html

    
    def test_scraper_saves_raw_rss_page(self):
        mock_page = self.get_mock_page()
        Scraper.save_rss_page(mock_page, MOCK_URL, MOCK_WEBSITE_NAME)
        self.assertEqual(RSSPage.objects.count(), 1)
        

    def test_scraper_cannot_save_rss_page_with_empty_fields(self):
        mock_page = self.get_mock_page()
        Scraper.save_rss_page('', MOCK_URL, MOCK_WEBSITE_NAME)
        Scraper.save_rss_page(mock_page, '', MOCK_WEBSITE_NAME)
        Scraper.save_rss_page(mock_page, MOCK_URL, '')
        self.assertEqual(RSSPage.objects.count(), 0)

    
    def test_scraper_saves_correct_number_of_rss_pages(self):
        Scraper.scrape_all()
        with open('scraper/static/websites_to_scrape.json') as file:
            data = json.load(file)
            website_count = len(data['websites'])
            print('~~~~~~~~~~~~~~~', website_count)
        self.assertEqual(RSSPage.objects.count(), website_count)


    def test_scraper_correctly_scrapes_webpage_from_parameters(self):
        website_params = {"name": MOCK_WEBSITE_NAME, "url": MOCK_HTML}
        Scraper.scrape_rss_page(website_params)
        self.assertEqual(RSSPage.objects.count(), 1)
        

    def test_scraper_retries_after_receiving_empty_html(self):
        self.fail()


class RSSPageTest(TestCase):

    def test_cannot_save_rss_page_with_empty_html(self):
        rss_page = RSSPage(html='', url=MOCK_URL, website_name=MOCK_WEBSITE_NAME)
        with self.assertRaises(ValidationError):
            rss_page.full_clean()
            rss_page.save()
        self.assertEqual(RSSPage.objects.count(), 0)