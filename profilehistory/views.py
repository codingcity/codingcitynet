from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
# Create your views here.





class ProfileList(ListView):
    model = Profile
    ordering = '-pk'

class ProfileDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
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
    fields = ['user_image', 'intro']#, 'created_at','thisuser']

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

