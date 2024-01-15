from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from rooms.models import Room
from posts.models import Post



class TestCommentViews(TestCase):
     
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



    # def test_create_comment_GET(self):
        
        
    #     response = self.client.get(reverse('create_comment', args=[1]))
        
    #     self.assertEquals(response.status_code, 302)