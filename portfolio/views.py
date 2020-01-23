from django.http import HttpResponse


def home(request):
	return HttpResponse('<h2> This is HomePage, Bitch </h2>')