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
