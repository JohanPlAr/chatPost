from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from registerLoginLogout.models import Profile


class TestAuthViews(TestCase):
     
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


    def test_register_view_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register_login.html')
    

    def test_login_GET(self):
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/register_login.html')


    def test_logoutUser_GET(self):
        """
        Test user is redirect running logoutUser
        """
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/authentication/login')


    def test_create_profile_GET(self):
        response = self.client.get(reverse('create_profile', args=[self.user.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registerLoginLogout/create_profile.html')

    def test_create_profile_unauthorized(self):
        """
        Test user cant edit another
        users profile
        """
        user_model = get_user_model()
        
        # Create second user for 403 errors
        username = 'dirty'
        password = 'deedster56'
        user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        logged_in = self.client.login(
            username=username,
            password=password
        )

        response = self.client.get(reverse('create_profile', args=[1]))
        self.assertEquals(response.status_code, 403)


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

    def test_create_profile_redirect_GET(self):
        """ Test redirect on create profile  """
        response = self.client.get('/authentication/profile/1')
        self.assertEqual(response.status_code, 302)
    
    def test_view_profile_redirect_GET(self):
        """ Test redirect on create profile  """
        response = self.client.get('/authentication/view-profile/1')
        self.assertEqual(response.status_code, 302)
        