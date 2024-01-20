"""Unitests for Post Views"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rooms.models import Room, Topic
from posts.models import Post
from comments.models import Comment


class TestPostsViews(TestCase):
    """Testing that Posts views correct 
    renders and redirects """

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

        Post.objects.create(author=self.user,
                            room=room,
                            content='Test-post-content',
                            )
        post = Post.objects.get(id=1)
        # Create Comment

        Comment.objects.create(author=self.user,
                               post=post,
                               content='Test-comment-content',
                               )

    def test_create_comment_get(self):
        """Test logged in user can render comment_form.html"""
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('create_comment', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comments/comment_form.html')

    def test_edit_comment_get(self):
        """ Test logged in user can render comment_form.html """
        comment = Comment.objects.get(id=1)
        response = self.client.get(reverse('edit_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comments/comment_form.html')

    def test_delete_comment_get(self):
        """ Test logged in user can render delete.html """
        comment = Comment.objects.get(id=1)
        response = self.client.get(reverse('delete_post', args=[comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    def test_like_comment_get(self):
        """ Test logged in user redirects to /room/1 """
        comment = Comment.objects.get(id=1)
        response = self.client.get(reverse('like_comment', args=[comment.id]))
        self.assertRedirects(response, '/room/1')

    def test_dislike_comment_get(self):
        """ Test logged in user redirects to /room/1 """
        comment = Comment.objects.get(id=1)
        response = self.client.get(
            reverse('dislike_comment', args=[comment.id]))
        self.assertRedirects(response, '/room/1')

    def test_edit_unauthorized(self):
        """
        Test user cant edit another
        user comment
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
        response = self.client.get('/room/post/comment/edit/1')
        self.assertEqual(response.status_code, 403)

    def test_delete_unauthorized(self):
        """
        Test user cant delete another
        user comment
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

        response = self.client.get('/room/post/comment/delete/1')

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 403)


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """

    def test_create_comment_auth_redirect(self):
        """ Test redirect on create comment  """
        response = self.client.get('/room/post/comment/create/1')
        self.assertEqual(response.status_code, 302)

    def test_edit_comment_auth_redirect(self):
        """ Test redirect on edit comment  """
        response = self.client.get('/room/post/comment/edit/1')
        self.assertEqual(response.status_code, 302)

    def test_delete_comment_auth_redirect(self):
        """ Test redirect on delete comment  """
        response = self.client.get('/room/post/comment/delete/1')
        self.assertEqual(response.status_code, 302)
