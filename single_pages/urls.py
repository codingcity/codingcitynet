from django.urls import path
from . import views

app_name = 'single_pages'

urlpatterns = [
    path('about_us/', views.about_us),
    path('', views.landing, name='index'),
]