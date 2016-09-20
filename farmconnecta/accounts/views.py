from django.shortcuts import render
from .models import UserProfile


# Create your views here.
def follow(request, pk):
    current_user = request.user
    follower = UserProfile.objects.get(id=pk)
    follower.follows.add(current_user)
    return render(request, 'account/follow-redirect.html', {'current_user': current_user, 'follower': follower})


# Create your views here.s
def unfollow(request, pk):
    current_user = request.user
    follower = UserProfile.objects.get(id=pk)
    follower.follows.remove(current_user)
    return render(request, 'account/follow-redirect.html', {'current_user': current_user, 'follower': follower})