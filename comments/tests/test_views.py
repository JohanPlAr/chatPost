from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model



class TestCommentViews(TestCase):
     

    def test_CreateComment_GET(self):
        """ Setup test """
        username = "johan"
        password = "1442Aert"
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)
        response = self.client.get(reverse('create_comment'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'comments/comment_form.html')

    


  