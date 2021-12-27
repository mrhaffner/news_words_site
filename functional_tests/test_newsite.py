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

        # Stevesie notices a list of the most popular words
        # appearing in the news

        ##loop through all items and make sure they are not empty?

        # Stevesie also sees a two lists showing word frequency
        # on right wing and left wing news sites 