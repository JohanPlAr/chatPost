"""Testing if Base Url resolves"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import home


class TestHomeUrls (SimpleTestCase):
    """ Check if the view function for the URL is 'home' """

    def test_home_url_resolves(self):
        """Tests if url loads correct view function"""
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)
