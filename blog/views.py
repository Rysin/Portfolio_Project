from django.shortcuts import render
from .models import Blog


# Create your views here.
def allblogs(request):
	# Be Careful about the relative paths. /blog/ is terrorism
	blogObjects = Blog.objects
	return render(request, 'blog/allblogs.html', {'blogObjects': blogObjects})
