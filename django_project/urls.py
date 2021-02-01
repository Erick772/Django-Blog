"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import ListView

from blog.views import post_view, index
from blog.models import Post

urlpatterns = [
	#path('', index, name='index'),
	path('', ListView.as_view(template_name='index.html', model=Post, paginate_by=3), name='index'),
	path('post/<post_id>/', post_view, name='post'),
    path('admin/', admin.site.urls),
]
