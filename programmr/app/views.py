from django.shortcuts import render,redirect,get_object_or_404
from django import http
from .models import Users
from .models import Questions
from .models import Submission
from .forms import ProfileForm
from django.http import *
from oauth2client.contrib.django_util import decorators
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib import quote_plus
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




def profile(request):
	email="nooreenharoon@gmail.com"
	
	form=ProfileForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
        
		
		return redirect("app:dashboard")
		
	else:
	 	
		context={
	     "form": form,
	}
	
	
	return render(request,"profile.html",context)



def dashboard(request):

	queryset=Questions.objects.all()
	context={
	     "object_list":queryset,
	}
	return render(request,"dashboard.html",context)

def rules(request):
	return render(request,"rules.html")
	
def announcements(request):
	return render(request,"announcements.html")
	

def question_detail(request,id=None):
	instance=get_object_or_404(Questions,id=id)
	
	
	context={
	      "instance":instance,
	    
	 }
	return render(request,"question_detail.html",context)

