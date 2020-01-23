from django.db import models


# Create your models here.
class Blog(models.Model):
	# Title
	title = models.CharField(max_length=100)
	# Publish Date: Last Modified will be shown
	date = models.DateField(auto_now_add=True)
	# Body
	blog_body = models.TextField()
	# Image
	image = models.ImageField(upload_to='blog_images/')
