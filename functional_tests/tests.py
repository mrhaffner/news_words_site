from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    
    def tearDown(self) -> None:
        self.browser.quit()
        

    def test_django_loads(self) -> None:
        self.browser.get('http://localhost:8000')

        self.assertIn('install worked', self.browser.title)