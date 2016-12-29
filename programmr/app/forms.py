from django import forms

from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=[
            "name",
            "email_ID",
            "avatar",
            "year",
            "branch",
            "mobile_no",
            
        ]