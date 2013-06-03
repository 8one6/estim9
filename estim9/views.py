from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from estim9.forms import LoginForm
	
def home(request):
	return render(request, 'home.html')

def profile(request):
	return render(request, 'accounts/profile.html')

def login_user(request):
	d = {}
	
	if request.user.is_authenticated(): #already logged in
		return HttpResponseRedirect('/accounts/profile')
	
	form = LoginForm(request.POST or None)
	d['login_form'] = form
	d['next'] = request.GET.get('next', '/accounts/profile')
	
	if request.method == 'POST': #submitting form
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active: #all good, log user in
					login(request, user)
					return HttpResponseRedirect(request.POST.get('next', None))
				else: #account disabled
					return HttpResponseRedirect('/accounts/disabled')
			else: #authenticate failed
				errorlist = []
				errorlist.append(u'Login failed, please try again.')
				d['errors'] = errorlist
				return render(request, 'accounts/login.html', d)
		else: #invalid form
			return render(request, 'accounts/login.html', d)
	else:  #display empty form
		return render(request, 'accounts/login.html', d)

@login_required
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')