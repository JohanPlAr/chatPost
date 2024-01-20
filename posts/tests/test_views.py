"""Testing Post Views"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rooms.models import Room, Topic
from posts.models import Post


class TestPostsViews(TestCase):
    """Testing Render and Redirects for Post Views"""
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

        # Create Room with Public Access to logged in users
        Room.objects.create(host=self.user,
                            topic=topic,
                            name='Test-room',
                            description='Test-room-description',
                            status=0,
                            )
        room = Room.objects.get(id=1)

        # Create Post

        Post.objects.create(author=self.user,
                            room=room,
                            content='Test-post-content',
                            )

    def test_create_post_get(self):
        """
        Test logged in user can render create post view
        """
        room = Room.objects.get(id=1)
        response = self.client.get(reverse('create_post', args=[room.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')

    def test_edit_post_get(self):
        """
        Test logged in user can render edit post view
        """
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('edit_post', args=[post.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_form.html')

    def test_edit_post_post(self):
        """ Test logged in user can post edited post"""
        room = Room.objects.get(id=1)
        post = Post.objects.get(id=1)
        url = reverse('edit_post', args=[post.id])
        response = self.client.post(url,
                                    {'author': self.user,
                                     'room': room,
                                     'content': 'Edited-Post-Content', })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/room/1')
        self.assertTrue(Post.objects.get(
            id=1).content == 'Edited-Post-Content')

    def test_delete_post_get(self):
        """
        Test logged in user can render delete post view
        """
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('delete_post', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    def test_like_post_get(self):
        """
        Test logged in user redirects when liking post
        """
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('like_post', args=[post.id]))
        self.assertRedirects(response, '/room/1')

    def test_dislike_post_get(self):
        """
        Test logged in user redirects when disliking post
        """
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('dislike_post', args=[post.id]))
        self.assertRedirects(response, '/room/1')

    def test_edit_unauthorized(self):
        """
        Test user can't edit another
        user post
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
        logged_in = self.client.login(
            username=username,
            password=password
        )

        self.assertTrue(logged_in)
        response = self.client.get('/room/post/edit/1')
        self.assertEqual(response.status_code, 403)

    def test_delete_unauthorized(self):
        """
        Test user cant delete another
        user post
        """
        user_model = get_user_model()

        # Create second user for 403 errors
        username1 = 'dirty'
        password1 = 'deedster56'
        user_model.objects.create_user(
            username=username1,
            password=password1,
            is_superuser=False
        )
        logged_in = self.client.login(
            username=username1,
            password=password1
        )

        response = self.client.get('/room/post/delete/1')

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 403)


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """

    def test_create_post_auth_redirect(self):
        """ Test unauthenticated user redirect on create post """
        response = self.client.get('/room/post/create/1')
        self.assertEqual(response.status_code, 302)

    def test_edit_post_auth_redirect(self):
        """ Test unauthenticated user redirect on edit post  """
        response = self.client.get('/room/post/edit/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_post_auth_redirect(self):
        """ Test unauthenticated user redirect on delete post  """
        response = self.client.get('/room/post/delete/1')
        self.assertEqual(response.status_code, 302)
