from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Categoryblog

from django.core.exceptions import PermissionDenied



class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'categoryblog']

    template_name = 'blog/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'head_image', 'file_upload', 'categoryblog']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

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

def categoryblog_page(request, slug):
    print('slug!!!!!!!!!!!!!!!!!',slug)
    if slug == 'no_category':
        categoryblog = '미분류'
        post_list = Post.objects.filter(categoryblog=None)
    else:
        categoryblog = Categoryblog.objects.get(slug=slug)
        post_list = Post.objects.filter(categoryblog=categoryblog)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categoriesblog': Categoryblog.objects.all(),
            'no_categoryblog_post_count': Post.objects.filter(categoryblog=None).count(),
            'categoryblog': categoryblog,
        }
    )
