from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('categoryblog/<str:slug>/', views.categoryblog_page),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
]