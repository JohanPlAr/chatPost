from django.test import SimpleTestCase
from django.urls import reverse, resolve
from comments.views import editComment, createComment, deleteComment, likeComment, dislikeComment
         
class TestCommentUrls (SimpleTestCase):

    def test_edit_comment_url_resolves(self):
         url = reverse('edit_comment', args=['some-comment.id'])
         self.assertEquals(resolve(url).func, editComment)
    
    
    def test_create_comment_url_resolves(self):
         url = reverse('create_comment', args=['some-post.id'])
         self.assertEquals(resolve(url).func, createComment)
    
    
    def test_delete_comment_url_resolves(self):
         url = reverse('delete_comment', args=['some-comment.id'])
         self.assertEquals(resolve(url).func, deleteComment)


    def test_like_comment_url_resolves(self):
         url = reverse('like_comment', args=['some-comment.id'])
         self.assertEquals(resolve(url).func, likeComment)


    def test_dislike_comment_url_resolves(self):
         url = reverse('dislike_comment', args=['some-comment.id'])
         self.assertEquals(resolve(url).func, dislikeComment)
         