from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from blog.models import Post
from boards.models import Question


def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    recent_questions = Question.objects.order_by('-pk')[:3]

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
            'recent_questions': recent_questions,
        }
    )


def about_us(request):
    return render(
        request,
        'single_pages/about_us.html'
    )