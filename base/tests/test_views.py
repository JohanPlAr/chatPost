"""Unitests for Base Views"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestBaseViews(TestCase):
    """Testing that Base views 
    renders"""

    def setUp(self):
        """ Setup test """
        username = "johan"
        password = "jbdwkbcwkc"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

    def test_home_get(self):
        """Test logged in user can render home.html"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')

    def test_home_unauthenticated_get(self):
        """
        Test unauthenticated user cant render home.html
        """
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
