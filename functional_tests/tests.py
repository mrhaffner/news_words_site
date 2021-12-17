from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    
    def tearDown(self) -> None:
        self.browser.quit()
        

    def test_can_view_top_news_words(self) -> None:
        # Stevesie has heard about a new web page that tracks
        # words used in the news.  He visits the homepage
        self.browser.get('http://localhost:8000')

        # He notices that that page title and header
        # mention News Words
        self.assertIn('Trending News Words', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Trending News Words', header_text)