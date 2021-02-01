from django.urls import path
from django.views.generic import ListView

from blog.views import PostView
from blog.models import Post

# As configurações das URLs ficam melhores dentro de cada app. Assim, quando o seu projeto tiver muitos apps, fica mais fácil fazer a manutenção.

urlpatterns = [
    path('', ListView.as_view(template_name='blog/base.html', model=Post, paginate_by=3), name='index'),
	path('post/<int:post_id>/', PostView.as_view(), name='post'),
]
