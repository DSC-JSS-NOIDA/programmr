from django import forms

from .models import UserProfile

class ProfileForm(forms.ModelForm):
    
    class Meta:
        
        model = UserProfile
        fields = [ "email_ID", "year", "branch", "mobile_no" ]
