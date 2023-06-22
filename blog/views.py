from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Categoryblog


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categoriesblog'] = Categoryblog.objects.all()
        context['no_categoryblog_post_count'] = Post.objects.filter(categoryblog=None).count()
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categoriesblog'] = Categoryblog.objects.all()
        context['no_categoryblog_post_count'] = Post.objects.filter(categoryblog=None).count()
        return context



