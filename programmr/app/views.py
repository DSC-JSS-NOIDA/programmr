from django.shortcuts import render
from django import http

from oauth2client.contrib.django_util import decorators

# Create your views here.
def login(request):
	return render(request, 'login.html')



@decorators.oauth_required
def google_login(request):
	resp, content = request.oauth.http.request('https://www.googleapis.com/plus/v1/people/me')
	return http.HttpResponse(content)



@decorators.oauth_enabled
def get_profile_optional(request):
	if request.oauth.has_credentials():
		return http.HttpResponse('User email: {}'.format(request.oauth.credentials.id_token['email']))
	else:
		return http.HttpResponse('Here is an OAuth Authorize link: <a href="{}"></a>'.format(request.oauth.get_authorize_redirect()))
