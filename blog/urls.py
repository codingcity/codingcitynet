from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('categoryblog/<str:slug>/', views.categoryblog_page),
]