from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from blog.models import Post, Comment
from boards.models import Question, Answer


def landing(request):

    recent_posts = Post.objects.order_by('-pk')[:3]
    recent_comments = Comment.objects.order_by('-pk')[:3]

    recent_questions = Question.objects.order_by('-pk')[:3]
    recent_answers = Answer.objects.order_by('-pk')[:3]

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
            'recent_comments': recent_comments,
            'recent_questions': recent_questions,
            'recent_answers': recent_answers,
        }
    )


def about_us(request):
    return render(
        request,
        'single_pages/about_us.html'
    )