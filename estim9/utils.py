from django.contrib import messages

def messages_from_form(request, form):
	for e in form.non_field_errors():
		messages.error(request, '<b>Error:</b> %s' % (e))
	for ewf in form.errors:
		for e in form[ewf].errors:
			messages.error(request, '<b>Error:</b> %s: %s' % (ewf.capitalize(), e))