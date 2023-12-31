"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from boards.views import base_views

from django.conf import settings
from django.conf.urls.static import static

from .settings import base


urlpatterns = [
    path('memo/', include('memo.urls')),
    path('profilehistory/', include('profilehistory.urls')),
    path('accounts/', include('allauth.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('boards/', include('boards.urls')),
    path('common/', include('common.urls')),
    path('', include('single_pages.urls')),
]

#    path('', base_views.index, name='index'),  # '/' 에 해당되는 path

handler404 = 'common.views.page_not_found'
handler413 = 'common.views.request_entity_too_large'
handler500 = 'common.views.internal_server_error'
handler502 = 'common.views.bad_gateway'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)

