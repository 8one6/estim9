from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from estim9.forms import LoginForm
	
def home(request):
	return render(request, 'home.html')

def profile(request):
	return render(request, 'account/profile.html')

def login_user(request):
	d = {}
	
	if request.user.is_authenticated(): #already logged in
		return HttpResponseRedirect('/account/profile')
	
	form = LoginForm(request.POST or None)
	d['login_form'] = form
	
	if request.method == 'POST': #submitting form
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active: #all good, log user in
					login(request, user)
					return HttpResponseRedirect('/account/profile')
				else: #account disabled
					return HttpResponseRedirect('/account/disable')
			else: #authenticate failed
				errorlist = []
				errorlist.append(u'Login failed, please try again.')
				d['errors'] = errorlist
				return render(request, 'account/login.html', d)
		else: #invalid form
			return render(request, 'account/login.html', d)
	else:  #display empty form
		return render(request, 'account/login.html', d)

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/account/login')