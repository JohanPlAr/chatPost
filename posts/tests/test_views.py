from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rooms.models import Room, Topic
from posts.models import Post


class TestPostsViews(TestCase):
     
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

        # Create Topic

        topic = Topic.objects.create(name='Test-topic')

        # Create Room
        Room.objects.create(host=self.user, 
                            topic=topic, 
                            name='Test-room', 
                            description='Test-room-description',
                            status=0,
                            )
        room = Room.objects.get(id=1)
        # Create Post

        Post.objects.create(author = self.user, 
                            room = room, 
                            content='Test-post-content',
                            )
        

    def test_create_post_GET(self):
        room = Room.objects.get(id=1)
        response = self.client.get(reverse('create_post', args=[room.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')
    
    
    def test_edit_post_GET(self):
        room = Room.objects.get(id=1)
        response = self.client.get(reverse('edit_post', args=[room.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')
    
    
    def test_delete_post_GET(self):
        room = Room.objects.get(id=1)
        response = self.client.get(reverse('delete_post', args=[room.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')
    
    def test_edit_unauthorized(self):
        """
        Test user cant edit another
        user room
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

        self.assertTrue(logged_in)
        response = self.client.get('/room/edit/1')
        self.assertEqual(response.status_code, 403)



    def test_delete_unauthorized(self):
        """
        Test user cant delete another
        user room
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

        response = self.client.get('/room/delete/1')

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 403)


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """
    def setUp(self):
        logged_out = self.client.logout()
        self.assertFalse(logged_out)
        

    def test_room_auth_redirect(self):
        """ Test redirect on view room  """
        response = self.client.get('/room/1')
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('base/register_login.html/')
    
    
    def test_create_room_auth_redirect(self):
        """ Test redirect on create room  """
        response = self.client.get('/room/create')
        self.assertEqual(response.status_code, 302)
       
    
    
    def test_edit_room_auth_redirect(self):
        """ Test redirect on edit room  """
        response = self.client.get('/room/edit/1')
        self.assertEqual(response.status_code, 302)
    
    
    def test_delete_room_auth_redirect(self):
        """ Test redirect on delete room  """
        response = self.client.get('/room/delete/1')
        self.assertEqual(response.status_code, 302)