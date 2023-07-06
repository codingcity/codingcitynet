from django.urls import path
from . import views

app_name = 'memo'


urlpatterns = [
    path('', views.PaperList.as_view(), name='index'),
    path('<int:pk>/', views.PaperDetail.as_view(), name='detail'),
    path('create_memo/', views.PaperCreate.as_view()),
]