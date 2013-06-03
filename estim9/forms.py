from django import forms

class LoginForm(forms.Form):
	username 		= forms.CharField(max_length=100, label=u'Username')
	username.widget.attrs['placeholder'] = u'Username'
	password		= forms.CharField(max_length=100, label=u'Password', widget=forms.PasswordInput)
	password.widget.attrs['placeholder'] = u'Password'