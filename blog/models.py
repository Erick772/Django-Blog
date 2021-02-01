from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)
	category = models.TextField(default='')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to='static')
	content = models.TextField()
