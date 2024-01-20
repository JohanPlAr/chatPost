"""Test Comment Urls"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from friends.views import accept_friend_request, remove_friend, friendRequest, friendsList
from registerLoginLogout.views import profileView


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
        """ Check if the view function for the URL is 'friendRequest' """
        url = reverse('friend_request', args=[FRIEND_REQUEST_ID])
        self.assertEqual(resolve(url).func, friendRequest)

    def test_friends_list_url_resolves(self):
        """ Check if the view function for the URL is 'friendslist' """
        url = reverse('friends_list')
        self.assertEqual(resolve(url).func, friendsList)

    def test_view_profile_url_resolves(self):
        """ Check if the view function for the URL is 'profileView' """
        url = reverse('view_profile', args=[FRIEND_REQUEST_ID])
        self.assertEqual(resolve(url).func, profileView)
