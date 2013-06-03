from django.shortcuts import render
from estim9.forms import LoginForm
	
def home(request):
	return render(request, 'home.html', {})
	
def login(request):
	if request.method == 'POST':
		pass
	else:
		form = LoginForm()
		return render(request, 'account/login.html', { 'login_form':form })