"""Test Posts Urls"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import (
    edit_post,
    create_post,
    delete_post,
    like_post,
    dislike_post
)


class TestPostsUrls (SimpleTestCase):
    """Testing if Urls resolves correct function"""

    def test_edit_post_url_resolves(self):
        """ Check if the view function for the URL is 'edit_post' """
        url = reverse('edit_post', args=['some-post.id'])
        self.assertEqual(resolve(url).func, edit_post)

    def test_create_post_url_resolves(self):
        """ Check if the view function for the URL is 'create_post' """
        url = reverse('create_post', args=['some-room.id'])
        self.assertEqual(resolve(url).func, create_post)

    def test_delete_post_url_resolves(self):
        """ Check if the view function for the URL is 'delete_post' """
        url = reverse('delete_post', args=['some-post.id'])
        self.assertEqual(resolve(url).func, delete_post)

    def test_like_post_url_resolves(self):
        """ Check if the view function for the URL is 'like_post' """
        url = reverse('like_post', args=['some-post.id'])
        self.assertEqual(resolve(url).func, like_post)

    def test_dislike_post_url_resolves(self):
        """ Check if the view function for the URL is 'dislike_post' """
        url = reverse('dislike_post', args=['some-post.id'])
        self.assertEqual(resolve(url).func, dislike_post)
