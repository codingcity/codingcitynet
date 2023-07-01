from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Categoryblog, Comment, Feedback
from django.shortcuts import get_object_or_404

from django.core.exceptions import PermissionDenied

from .forms import CommentForm, FeedbackForm
from django.db.models import Q

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
    paginate_by = 5

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
        context['comment_form'] = CommentForm
        context['feedback_Form'] = FeedbackForm
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


def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post

    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(content__contains=q)
        ).distinct()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context



def new_feedback(request, pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=pk)

        if request.method == 'POST':
            feedback_form = FeedbackForm(request.POST)
            if feedback_form.is_valid():
                feedback = feedback_form.save(commit=False)
                feedback.comment = comment
                feedback.author = request.user
                feedback.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(comment.get_absolute_url())
    else:
        raise PermissionDenied



class FeedbackUpdate(LoginRequiredMixin, UpdateView):
    model = Feedback
    form_class = FeedbackForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(FeedbackUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    comment = feedback.comment

    if request.user.is_authenticated and request.user == feedback.author:
        feedback.delete()
        return redirect(comment.get_absolute_url())
    else:
        raise PermissionDenied