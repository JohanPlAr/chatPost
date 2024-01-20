"""Test Comment Urls"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from friends.views import (
    accept_friend_request,
    remove_friend,
    friend_request_view,
    friends_list_view
    )
from registerLoginLogout.views import profile_view


FRIEND_REQUEST_ID = 99999


class TestCommentUrls (SimpleTestCase):
    """Testing if Urls resolves correct function"""

    def test_accept_friend_request_url_resolves(self):
        """ Check if the view function for the URL is 'accept_friend_request' """
        url = reverse('accept_friend_request', args=[FRIEND_REQUEST_ID])
        self.assertEqual(resolve(url).func, accept_friend_request)

    def test_remove_friend_url_resolves(self):
        """ Check if the view function for the URL is 'remove_friend' """
        url = reverse('remove_friend', args=[FRIEND_REQUEST_ID])
        self.assertEqual(resolve(url).func, remove_friend)

    def test_friend_request_url_resolves(self):
        """ Check if the view function for the URL is 'friend_request_view' """
        url = reverse('friend_request', args=[FRIEND_REQUEST_ID])
        self.assertEqual(resolve(url).func, friend_request_view)

    def test_friends_list_url_resolves(self):
        """ Check if the view function for the URL is 'friends_list' """
        url = reverse('friends_list')
        self.assertEqual(resolve(url).func, friends_list_view)

    def test_view_profile_url_resolves(self):
        """ Check if the view function for the URL is 'profile_view' """
        url = reverse('view_profile', args=[FRIEND_REQUEST_ID])
        self.assertEqual(resolve(url).func, profile_view)
