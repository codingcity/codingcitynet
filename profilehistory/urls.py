from django.urls import path
from . import views

app_name = 'profilehistory'

urlpatterns = [
    path('', views.ProfileList.as_view(), name='index'),
    path('<int:pk>/', views.ProfileDetail.as_view(), name='detail'),
    path('create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('<str:userid>/', views.profile_find, name='profile_find'),

]

