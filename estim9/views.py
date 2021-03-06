from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
import random
from estim9.forms import LoginForm
from estim9.utils import messages_from_form
	
def home(request):
	return render(request, 'home.html')


@login_required
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
					return HttpResponseRedirect(request.POST.get('next'))
				else: #account disabled
					return HttpResponseRedirect('/accounts/disabled')
			else: #authenticate failed
				messages.error(request, '<b>Error:</b> Login failed, please try again.')
				return render(request, 'accounts/login.html', d)
		else: #invalid form
			messages_from_form(request, form)
			return render(request, 'accounts/login.html', d)
	else:  #display empty form
		return render(request, 'accounts/login.html', d)


@login_required
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required
def test_view(request):
	for i in range(1,5):
		if random.random() > 0.5:
			messages.info(request, 'Error, dude!')
	breadcrumbs = [['Home', '/'], ['Away']]
			
	return render(request, 'test.html', {'breadcrumbs':breadcrumbs})
