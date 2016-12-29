from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy, reverse
from models import *
from forms import ProfileForm
from django.http import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib import quote_plus
from google_script import *
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

getGoogle = GooglePlus(settings.GOOGLE_PLUS_APP_ID, settings.GOOGLE_PLUS_APP_SECRET)


def login_page(request):
	
	if request.user.is_active:
		return render(request, 'dashboard.html')
	return render(request, 'login.html')



def login_google(request):

	google_url = getGoogle.get_authorize_url()
	return HttpResponseRedirect(google_url)



def google_login(request):

	code = request.GET['code']
	state = request.GET['state']
	getGoogle.get_access_token(code, state)
	userInfo = getGoogle.get_user_info()
	username = userInfo['given_name'] + userInfo['family_name']
	password = 'password'

	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		new_user = User.objects.create_user(username)
		new_user.set_password(password)
		new_user.save()

		try:
			profile = GoogleProfile.objects.get(user=new_user.id)
			profile.access_token = getGoogle.access_token
		except:
			profile = GoogleProfile()
			profile.user = new_user
			profile.google_user_id = userInfo['id']
			profile.access_token = getGoogle.access_token
			profile.profile_url = userInfo['link']
		profile.save()
	
	user = authenticate(username=username, password=password)
	login(request, user)
	return HttpResponseRedirect(reverse_lazy('dashboard'))



def logout_view(request):

	if request.user.is_active:
		logout(request)
		return HttpResponseRedirect(reverse_lazy('login_page'))
	else:
		return HttpResponseRedirect(reverse_lazy('dashboard'))




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

	if not request.user.is_active:
		return HttpResponseRedirect(reverse_lazy('login_page'))
	queryset = Question.objects.raw('select a.*, count(*) as totalsub from app_questions a, app_submission b where a.id=b.question_id and b.status=0 group by a.id')
	return render(request, 'dashboard.html')




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

