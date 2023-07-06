from django.shortcuts import render, redirect
from .models import Paper
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class PaperList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Paper
    ordering = '-pk'

    def test_func(self):
        return self.request.user.is_authenticated

class PaperDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Paper

    def test_func(self):
        return self.request.user.is_authenticated

class PaperCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Paper
    fields = ['receiver', 'content']

    def test_func(self):
        #return self.request.user.is_superuser or self.request.user.is_staff
        return self.request.user.is_authenticated

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated :#and (current_user.is_staff or current_user.is_superuser):
            form.instance.sender = current_user
            return super(PaperCreate, self).form_valid(form)
        else:
            return redirect('/memo/')