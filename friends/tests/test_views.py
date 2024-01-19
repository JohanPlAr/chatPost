"""Testing Friends Views"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from friends.models import FriendRequest
from registerLoginLogout.models import Profile


class TestFriendsViews(TestCase):
    """Testing that Friends Views 
    render and redirects correctly"""

    def setUp(self):
        """ Setup test """
        username = "johan"
        password = "jbdwkbcwkc"
        user_model = get_user_model()
        # Create user1
        self.user1 = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=False
        )
        # Create profile1
        Profile.objects.create(user=self.user1)
        profile1 = Profile.objects.get(user_id=1)
        self.assertTrue(profile1)

        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create user2
        username2 = "Dirty"
        password2 = "Deedster56"
        self.user2 = user_model.objects.create_user(
            username=username2,
            password=password2,
            is_superuser=False
        )
        # Create profile2
        Profile.objects.create(user=self.user2)
        profile2 = Profile.objects.get(user_id=2)
        self.assertTrue(profile2)
        # Create user3
        username3 = "Evil"
        password3 = "Knievel13"
        self.user3 = user_model.objects.create_user(
            username=username3,
            password=password3,
            is_superuser=False
        )

        # Create profile3
        Profile.objects.create(user=self.user3)
        profile3 = Profile.objects.get(user_id=3)
        self.assertTrue(profile3)

    def test_friend_list_GET(self):
        """Test logged in user can render friend_list"""
        response = self.client.get(reverse('friends_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'friends/friends.html')

    def test_friends_request_GET(self):
        """Test logged in user can create friend request
          and redirects to friends list"""
        response = self.client.get(
            reverse('friend_request', args=[self.user2.id]))
        self.assertRedirects(response, '/friend/list')
        self.assertTrue(FriendRequest.objects.get(id=1))

    def test_accept_friend_request_GET(self):
        """Test logged in user can accept friend request
         and render friendslist """
        # Create friend_request
        FriendRequest.objects.create(sender=self.user2,
                                     receiver=self.user1,
                                     status=0)
        friend_request = FriendRequest.objects.get(id=1)
        response = self.client.get(
            reverse('accept_friend_request', args=[friend_request.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'friends/friends.html')

    def test_remove_friend_GET(self):
        """ Test logged in user can render delete.html """
        # Create friend_request
        FriendRequest.objects.create(sender=self.user2,
                                     receiver=self.user1,
                                     status=1)
        friend_request = FriendRequest.objects.get(id=1)
        response = self.client.get(
            reverse('remove_friend', args=[friend_request.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

    def test_view_profile_GET(self):
        """Test logged in user render """
        response = self.client.get(
            reverse('view_profile', args=[self.user1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registerLoginLogout/profile.html')

    def test_accept_friend_request_unauthorized(self):
        """
        Test user cant accept a request
        not received by user
        """
        FriendRequest.objects.create(sender=self.user1,
                                     receiver=self.user2,
                                     status=0)
        friend_request = FriendRequest.objects.get(id=1)
        response = self.client.get(
            reverse('accept_friend_request', args=[friend_request.id]))
        self.assertEqual(response.status_code, 403)

    def test_remove_friend_unauthorized(self):
        """
        Test user cant remove another users friend or requests
        """
        username3 = "Evil"
        password3 = "Knievel13"
        logged_in = self.client.login(username=username3, password=password3)
        self.assertTrue(logged_in)

        FriendRequest.objects.create(sender=self.user1,
                                     receiver=self.user2,
                                     status=0)
        friend_request = FriendRequest.objects.get(id=1)
        response = self.client.get(
            reverse('remove_friend', args=[friend_request.id]))
        self.assertEqual(response.status_code, 403)


class TestRedirectViews(TestCase):
    """
    Test views when not logged in
    """

    def test_friends_list_redirect_GET(self):
        """Test logged out user cant render friends_list"""
        response = self.client.get(reverse('friends_list'))
        self.assertEqual(response.status_code, 302)

    def test_accept_friend_request_redirect_GET(self):
        """Test logged out user cant accept friend request"""
        response = self.client.get(reverse('accept_friend_request', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_remove_friend_redirect_GET(self):
        """Test logged out user cant remove friend/request"""
        response = self.client.get(reverse('remove_friend', args=[1]))
        self.assertEqual(response.status_code, 302)
