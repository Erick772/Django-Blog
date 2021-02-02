from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView

from .models import Post

class PostView(TemplateView):
	template_name = 'blog/single.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		if 'post_id' in kwargs.keys():
			if not Post.objects.filter(id=kwargs['post_id']).exists():
				raise Http404
			else:
				context['post'] = Post.objects.get(id=kwargs['post_id'])

		return context
