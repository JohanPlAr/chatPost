from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from registerLoginLogout.views import loginView, logoutUser, registerView, createProfile, profileView

class TestAuthUrls (TestCase):

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
         self.assertEquals(resolve(url).func, loginView)
    
    
    def test_logout_url_resolves(self):
         url = reverse('logout')
         self.assertEquals(resolve(url).func, logoutUser)
    
    
    def test_register_url_resolves(self):
         url = reverse('register')
         self.assertEquals(resolve(url).func, registerView)


    def test_create_profile_url_resolves(self):
         url = reverse('create_profile', args=[self.user.id])
         self.assertEquals(resolve(url).func, createProfile)


    def test_view_profile_url_resolves(self):
         url = reverse('view_profile', args=[self.user.id])
         self.assertEquals(resolve(url).func, profileView)
         