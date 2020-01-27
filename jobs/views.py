from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
	# Import Job Objects
	jobs = Job.objects
	# Add reference to jobObjects to HTML to be rendered.
	return render(request, 'jobs/home.html', {'jobs': jobs})
