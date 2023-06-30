from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import User

# Create your views here.





class ProfileList(ListView):
    model = Profile
    ordering = '-pk'

class ProfileDetail(DetailView):#,UserPassesTestMixin,LoginRequiredMixin,
    model = Profile

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.thisuser = current_user
            response = super(ProfileCreate, self).form_valid(form)

            return response
        else:
            return redirect('/profileHistory/')

class ProfileCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Profile
    fields = ['user_image', 'intro', 'public_approved', 'birthdate']#, 'created_at','thisuser']

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.thisuser = current_user
            response = super(ProfileCreate, self).form_valid(form)

            return response
        else:
            return redirect('/profileHistory/')



def profile_find(request, userid):

    """
    print('????????????userid',userid)
    info1 =User.objects.get(username=userid)
    print('???????????!!!!?info1', info1)

    info = Profile.objects.get(public_approved=True, thisuser=info1)
    print('!!!!!!!!!!!!!!!!',info)
    profile_list = Profile.objects.filter(thisuser=info)

    profile_list = Profile.objects.get(public_approved=True)
    print('!!!!!!!!!!!!!!!!',profile_list)


    info = get_object_or_404(Profile, userid=userid)
    print('!!!!!!!!!!!!!!!!', info)
    profile_list = Profile.objects.filter(thisuser=info)

    print('!!!!!!!!!!!!!!!!', userid)
    username = User.objects.filter(id=userid)

    """
    username = User.objects.get(username=userid)
    print('!!!!!!!!!!!!!!!!', username.id)


    profile_list = Profile.objects.filter(thisuser=username.id )
    print('!!!!!!!!!!!!!!!!', profile_list)


    profile_list = Profile.objects.filter(public_approved=True) & Profile.objects.filter(thisuser=username.id )
    print('!!!!!!!!!!!!!!!!', profile_list)

    is_userid = True

    userid_in_view = userid

    return render(
        request,
        'profilehistory/profile_list.html',
        {
            'profile_list': profile_list,
            'is_userid': is_userid,
            'userid_in_view': userid_in_view,
        }
    )