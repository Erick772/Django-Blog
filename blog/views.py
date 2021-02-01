from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
	return render(request, 'index.html')

def post_view(request, post_id):
	if Post.objects.filter(id=post_id).count() == 0:
		return HttpResponse('Erro 404: página não encontrada.')
	
	context = {
		'POST': Post.objects.get(id=post_id)
	}
	
	return render(request, 'single.html', context)
