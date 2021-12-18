from django.test import TestCase


class HomePageTest(TestCase):

    def test_site_resolves(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')