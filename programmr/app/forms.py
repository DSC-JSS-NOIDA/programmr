from django import forms

from .models import Users

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=[
            "name",
            "email_ID",
            "avatar",
            "year",
            "branch",
            "mobile_no",
            
        ]