from django import forms

from .models import *

class ProfileForm(forms.ModelForm):

	class Meta:

		model = UserProfile
		fields = ['year', 'branch', 'mobile_no']


class UploadFileForm(forms.Form):
	file = forms.FileField(required=False)
