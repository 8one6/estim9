from django.shortcuts import render

def hello(request):
	return render(request, 'base.html', {})

def home(request):
	return render(request, 'base.html', {})