from django.db import models


class Job(models.Model):
	# Store Images to DB
	image = models.ImageField(upload_to='blog_images/')
	summary = models.CharField(max_length=200)
