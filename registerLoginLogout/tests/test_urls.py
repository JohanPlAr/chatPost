"""Test Profile and authentication urls"""
from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from registerLoginLogout.views import (
    login_view,
    logout_user,
    register_view,
    create_profile,
    profile_view
)


class TestAuthUrls (TestCase):
     """Testing that urls resolves correctly"""
     def setUp(self):
        """ Setup test """
        username = "johan"
        password = "jbdwkbcwkc"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        return self.user.id

     def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_view)

     def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)

     def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_view)

     def test_create_profile_url_resolves(self):
        url = reverse('create_profile', args=[self.user.id])
        self.assertEqual(resolve(url).func, create_profile)

     def test_view_profile_url_resolves(self):
        url = reverse('view_profile', args=[self.user.id])
        self.assertEqual(resolve(url).func, profile_view)
