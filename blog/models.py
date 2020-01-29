from django.db import models


# Create your models here.
class Blog(models.Model):
	# Title
	title = models.CharField(max_length=100)
	# Publish Date: Last Modified will be shown
	date = models.DateField()
	# Summary
	summary = models.TextField()
	# Body
	body = models.TextField()
	# Image
	image = models.ImageField(upload_to='blog_images/')
	
	def __str__(self):
		return self.title
