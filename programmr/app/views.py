from django.shortcuts import render,redirect
from .models import Users
from .forms import ProfileForm

from .models import Users
from django.http import *


# Create your views here.

def home(request):
	return render(request,"home.html")

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
	#check auth user
	return render(request,"dashboard.html")

def rules(request):
	return render(request,"rules.html")
	
def announcements(request):
	return render(request,"announcements.html")
	
	
