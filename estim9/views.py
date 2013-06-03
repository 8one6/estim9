from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from estim9.forms import LoginForm
	
def home(request):
	return render(request, 'home.html')
	
def login(request):
	context = {}
	
	if request.user.is_authenticated(): #already logged in
		return HttpResponseRedirect('/account/profile')
	
	form = LoginForm(request.POST or None)
	context['login_form'] = form
	
	if request.method == 'POST': #submitting form
		if form.is_valid():
			context['content'] = form.cleaned_data
			return render(request, 'test.html', context)
		else: #invalid form
			return render(request, 'account/login.html', context)
	else:  #display empty form
		return render(request, 'account/login.html', context)