import requests
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from models import *
from forms import *
from django.http import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib import quote_plus
from google_script import *
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from urllib import urlopen


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
	new = None

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
			new = True
			user_profile = UserProfile()
			user_profile.user = new_user
			user_profile.name = username
			user_profile.avatar = userInfo['picture']
		
		profile.save()
		user_profile.save()
	
	user = authenticate(username=username, password=password)
	login(request, user)
	
	if new == True:
		return HttpResponseRedirect(reverse_lazy('profile'))
	
	return HttpResponseRedirect(reverse_lazy('dashboard'))



def logout_view(request):

	if request.user.is_active:
		logout(request)
	
	return HttpResponseRedirect(reverse_lazy('login_page'))



def profile(request):

	if not request.user.is_active:
		return HttpResponseRedirect(reverse_lazy('login_page'))

	a = UserProfile.objects.get(user=request.user)
	f = ProfileForm(request.POST, instance=a)
	
	if request.method == 'POST':
		print "saved!"
		f.save()
		return HttpResponseRedirect(reverse_lazy('dashboard'))

	return render(request, 'profile.html', {'form': f, 'user': a})



def dashboard(request):
	
	if not request.user.is_active:
		return HttpResponseRedirect(reverse_lazy('login_page'))
	
	user_detail = UserProfile.objects.get(user=request.user)
	queryset=Question.objects.all()

	
	context={ "user": user_detail, "questions":queryset }
	
	return render(request, "dashboard.html", context)



def question_detail(request,id=None):
	
	if not request.user.is_active:
		return HttpResponseRedirect(reverse_lazy('login_page'))

	instance=get_object_or_404(Question,id=id)
	form = UploadFileForm()
	context={ "question": instance, "form": form }
	return render(request, "question_detail.html", context)



def rules(request):
	return render(request,"rules.html")


	
def announcements(request):
	return render(request,"announcements.html")
	




def submission(request,id=None):

	#! -*- coding: utf-8 -*-
	#import string

	if not request.user.is_active:
		
		return HttpResponseRedirect(reverse_lazy('login_page'))

	elif request.method == 'POST':
		
		user_detail = UserProfile.objects.get(user=request.user)
		user_id = user_detail.email_ID

		id = request.POST['id']
		instance = get_object_or_404(Question, id=id)

		# constants
		RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
		CLIENT_SECRET = 'b00a3022083cfb5ba5fc2377d0d126e612c35d82'

		lang = request.POST['lang']

		if len(request.POST['source']) != 0:
			
			source = request.POST['source']
			print source

			data = {
		    	'client_secret': CLIENT_SECRET,
		    	'async': 0,
		    	'source': source,
		    	'lang': lang,
		    	'time_limit': 5,
		    	'memory_limit': 262144,
		    	'input':instance.testcase_input,
			}

		elif len(request.FILES) != 0:
			form = UploadFileForm(request.POST, request.FILES)
			if form.is_valid():
				file = request.FILES['file']
				source = file.read()

				data = {
			    	
			    	'client_secret': CLIENT_SECRET,
			    	'async': 0,
			    	'source': source,
			    	'lang': lang,
			    	'time_limit': 5,
			    	'memory_limit': 262144,
			    	'input':instance.testcase_input,
				}

		print data
		r = requests.post(RUN_URL, data=data)
		status = r.json()
		print status
		status=status['run_status']
		status=status['status']
		output = None


		web_link=r.json()
		web_link=web_link['web_link']

		f = Question.objects.all().get(id=id).testcase_input
		f.open(mode='rb') 
		lines_input = f.readlines()
		f.close()

		g = Question.objects.all().get(id=id).testcase_output
		g.open(mode='rb') 
		lines_output = g.readlines()
		g.close()
		
		
		str1 = ''.join(str(e) for e in lines_output)




		if(status=="CE"):
			result=0
		elif(status=="TLE"):
			result=1
		elif(status=="RE"):
			result=2
		else:
			output = r.json()
			output=output['run_status']
			output=output['output']


			if output == str1:
				result = 4
				# correct answer
			else:
				result=3
				# wrong answer


		query = Submission(user_ID=user_id, question_ID=id, status=result,source_code_URL=web_link)
		temp=query.save()

		
		q=Submission.objects.extra(where=["question_ID="+id,"status=4","user_ID=user_id"]).count
		
		
	

		context={
		"object":r.json(),
	    "data1":result,
		"language":lang,
		"source":source,
		"data":web_link,
		"user":user_detail.email_ID,
		"temp":temp,
		#"entry":entry,
		"q":q,
		"lines_input":lines_input,
		"lines_output":lines_output,
		"str1":str1,
		}
		
		return render(request,"submission.html",context)

	else:
		return render(request,"error.html",context)




def leaderboard(request):
	data=UserProfile.objects.annotate().order_by('-total_score')
	
    
	context={
    "data":data,
    }
	return render(request,"leaderboard.html",context)