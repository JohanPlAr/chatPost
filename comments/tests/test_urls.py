"""Test comment Urls"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from comments.views import (
    edit_comment,
    create_comment,
    delete_comment,
    like_comment,
    dislike_comment
)


class TestCommentUrls (SimpleTestCase):
    """Test if Url calls correct function"""

    def test_edit_comment_url_resolves(self):
        """Test if Url calls correct function"""
        url = reverse('edit_comment', args=['some-comment.id'])
        self.assertEqual(resolve(url).func, edit_comment)

    def test_create_comment_url_resolves(self):
        """Test if Url calls correct function"""
        url = reverse('create_comment', args=['some-post.id'])
        self.assertEqual(resolve(url).func, create_comment)

    def test_delete_comment_url_resolves(self):
        """Test if Url calls correct function"""
        url = reverse('delete_comment', args=['some-comment.id'])
        self.assertEqual(resolve(url).func, delete_comment)

    def test_like_comment_url_resolves(self):
        """Test if Url calls correct function"""
        url = reverse('like_comment', args=['some-comment.id'])
        self.assertEqual(resolve(url).func, like_comment)

    def test_dislike_comment_url_resolves(self):
        """Test if Url calls correct function"""
        url = reverse('dislike_comment', args=['some-comment.id'])
        self.assertEqual(resolve(url).func, dislike_comment)
