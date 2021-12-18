from django.test import TestCase
from django.urls import resolve

from news_site.views import home_page


class HomePageTest(TestCase):

    def test_site_resolves(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)