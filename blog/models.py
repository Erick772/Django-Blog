from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=50)
	order = models.IntegerField(default=999)	# Sugestão: Campo para definir a ordem em que as categorias aparecem no admin

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'categories'

class Post(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField(default=timezone.now)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='media/posts')	# Usar uma pasta separada para media é melhor e você pode criar pastas separadas para cada tipo de mídia (media/posts, media/users, etc)
	content = models.TextField()

	def __str__(self):
		return self.title
