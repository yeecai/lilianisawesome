from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Token
from django.core.urlresolvers import reverse
# Create your views here.


#send_login_email views and redirect to homepage later
def send_login_email(request):
	email = request.POST['email']
	token=Token.objects.create(email=email)
	url=request.build_absolute_uri(
		reverse('login')+'?token='+str(token.uid)
	)
	message_body=f'Use this link to log in:\n\n{url}'

	send_mail(
		'Your log in link from todolist',
		message_body,
		'test@mockfrom.com',
		[email],
	)
	messages.success(
		request,
		"Check your email, we've sent you a link you can use to log in."
	)
	return redirect('/')

def login(self):
	return redirect('/')		
