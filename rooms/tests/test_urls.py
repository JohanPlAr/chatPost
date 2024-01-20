"""Test Comment Urls"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rooms.views import edit_room, create_room, delete_room, room


class TestCommentUrls (SimpleTestCase):
    """Testing that urls resolves correctly"""

    def test_room_url_is_resolves(self):
        """ Check if the view function for the URL is 'room' """
        url = reverse('room_id', args=[0])
        self.assertEqual(resolve(url).func, room)

    def test_edit_room_url_is_resolves(self):
        """ Check if the view function for the URL is 'edit_room' """
        url = reverse('edit_room', args=['some-room.id'])
        self.assertEqual(resolve(url).func, edit_room)

    def test_delete_room_url_is_resolves(self):
        """ Check if the view function for the URL is 'delete_room' """
        url = reverse('delete_room', args=['some-room.id'])
        self.assertEqual(resolve(url).func, delete_room)

    def test_create_room_url_is_resolves(self):
        """ Check if the view function for the URL is 'create_room' """
        url = reverse('create_room')
        self.assertEqual(resolve(url).func, create_room)
