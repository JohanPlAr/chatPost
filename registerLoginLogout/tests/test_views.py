"""Test of profile and auth views"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from registerLoginLogout.models import Profile


class TestAuthViews(TestCase):
    """Testing Render and Redirects for 
    Profile and Authentication Views"""

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
        # Create profile
        Profile.objects.create(user=self.user)
        profile = Profile.objects.get(user_id=1)
        self.assertTrue(profile)

    def test_register_view_get(self):
        """
        Test logged in user can render correct view
        """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register_login.html')

    def test_login_get(self):
        """
        Test logged in user can render correct view
        """
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register_login.html')

    def test_logout_user_get(self):
        """
        Test user is redirects logoutUser
        """
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/authentication/login')

    def test_create_profile_get(self):
        """
        Test logged in user can render correct view
        """
        response = self.client.get(
            reverse('create_profile', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'registerLoginLogout/create_profile.html')

    def test_create_profile_unauthorized(self):
        """
        Test user cant edit another
        users profile
        """
        user_model = get_user_model()

        # Create second user for 403 errors
        username = 'dirty'
        password = 'deedster56'
        user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        self.client.login(
            username=username,
            password=password
        )

        response = self.client.get(reverse('create_profile', args=[1]))
        self.assertEqual(response.status_code, 403)


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """

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

        # Create profile
        Profile.objects.create(user=self.user)
        profile = Profile.objects.get(user_id=1)
        self.assertTrue(profile)

    def test_create_profile_redirect_get(self):
        """ Test redirect on create profile  """
        response = self.client.get('/authentication/profile/1')
        self.assertEqual(response.status_code, 302)

    def test_view_profile_redirect_get(self):
        """ Test redirect on create profile  """
        response = self.client.get('/authentication/view-profile/1')
        self.assertEqual(response.status_code, 302)
