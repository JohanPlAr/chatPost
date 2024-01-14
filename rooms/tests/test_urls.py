from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rooms.views import editRoom, createRoom, deleteRoom, room

class TestCommentUrls (SimpleTestCase):


    def test_room_url_is_resolves(self):
         url = reverse('room_id', args=[9999])
         self.assertEquals(resolve(url).func, room)

    
    def test_edit_room_url_is_resolves(self):
         url = reverse('edit_room', args=['some-room.id'])
         self.assertEquals(resolve(url).func, editRoom)
    
    
    def test_delete_room_url_is_resolves(self):
         url = reverse('delete_room', args=['some-room.id'])
         self.assertEquals(resolve(url).func, deleteRoom)
    
    
    def test_create_room_url_is_resolves(self):
         url = reverse('create_room')
         self.assertEquals(resolve(url).func, createRoom)
    
