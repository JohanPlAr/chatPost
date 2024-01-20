"""Context processor"""
from registerLoginLogout.models import Profile
from rooms.models import Room, Topic
from posts.models import Post
from comments.models import Comment
from friends.models import FriendRequest





def global_context(request):
    """Captures and sends the context to all views, 
module included in settings TEMPLATES"""
    rooms = Room.objects.all()
    room_count = rooms.count()
    topics = Topic.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    friend_data = FriendRequest.objects.all()
    friends_list = []
    friend_profiles = []
    profiles = Profile.objects.all()
    all_requests = FriendRequest.objects.all()
    if request.user.is_authenticated:
        users_rooms = Room.objects.filter(host=request.user)
        received_requests = FriendRequest.objects.filter(
            receiver=request.user, status=0)
        sent_requests = FriendRequest.objects.filter(
            sender=request.user, status=0)
        accepted_received_requests = FriendRequest.objects.filter(
            receiver=request.user, status=1)
        accepted_sent_requests = FriendRequest.objects.filter(
            sender=request.user, status=1)
        number_of_friends = accepted_received_requests.count() + \
            accepted_sent_requests.count()
        for instance in accepted_sent_requests:
            friends_list.append(instance.receiver)
            pk = instance.receiver.id
            friend_profile = Profile.objects.get(pk=pk)
            friend_profiles.append(friend_profile)
        for instance in accepted_received_requests:
            friends_list.append(instance.sender)
            pk = instance.sender.id
            friend_profile = Profile.objects.get(pk=pk)
            friend_profiles.append(friend_profile)

        return {
            'posts': posts,
            'comments': comments,
            'topics': topics,
            'rooms': rooms,
            'users_rooms': users_rooms,
            'room_count': room_count,
            'friend_data': friend_data,
            'all_requests': all_requests,
            'friends_list': friends_list,
            'number_of_friends': number_of_friends,
            'sent_requests': sent_requests,
            'received_requests': received_requests,
            'profiles': profiles,
            'friend_profiles': friend_profiles

        }
    else:
        return {
            'posts': posts,
            'comments': comments,
            'topics': topics,
            'rooms': rooms,
            'room_count': room_count,
            'friend_data': friend_data,
            'all_requests': all_requests,
            'profiles': profiles,
        }
