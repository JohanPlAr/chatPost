from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import editPost, createPost, deletePost, likePost, dislikePost
         
class TestPostsUrls (SimpleTestCase):

    def test_edit_Post_url_resolves(self):
         """ Check if the view function for the URL is 'editPost' """
         url = reverse('edit_post', args=['some-post.id'])
         self.assertEquals(resolve(url).func, editPost)
    
    
    def test_create_post_url_resolves(self):
         """ Check if the view function for the URL is 'createPost' """
         url = reverse('create_post', args=['some-room.id'])
         self.assertEquals(resolve(url).func, createPost)
    
    
    def test_delete_post_url_resolves(self):
         """ Check if the view function for the URL is 'deletePost' """
         url = reverse('delete_post', args=['some-post.id'])
         self.assertEquals(resolve(url).func, deletePost)


    def test_like_post_url_resolves(self):
         """ Check if the view function for the URL is 'likePost' """
         url = reverse('like_post', args=['some-post.id'])
         self.assertEquals(resolve(url).func, likePost)


    def test_dislike_post_url_resolves(self):
         """ Check if the view function for the URL is 'dislikePost' """         
         url = reverse('dislike_post', args=['some-post.id'])
         self.assertEquals(resolve(url).func, dislikePost)
         