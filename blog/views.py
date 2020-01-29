from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog


# Create your views here.
def allblogs(request):
	# Be Careful about the relative paths. /blog/ is terrorism
	blogObjects = Blog.objects
	return render(request, 'blog/allblogs_final.html', {'blogObjects': blogObjects})


def details(request, blog_id):
	blogDetails = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/details.html', {'blogDetails': blogDetails})
