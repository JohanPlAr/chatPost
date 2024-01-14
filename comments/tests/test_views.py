from django.test import TestCase, Client
from django.urls import reverse


class TestCommentViews(TestCase):
     

    def test_create_comment_GET(self):
        client = Client()
        
        response = client.get(reverse('create_comment', args=['some-post.id']))
        
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'comments/comment_form.html')
        
    


  