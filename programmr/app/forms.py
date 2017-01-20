from django.forms import Form, ModelForm, TextInput, FileField

from .models import *

class ProfileForm(ModelForm):

	class Meta:

		model = UserProfile
		fields = ['year', 'branch', 'mobile_no']
		widgets = {
            'year': TextInput(attrs={'placeholder': 'Year'}),
            'branch': TextInput(attrs={'placeholder': 'Branch'}),
            'mobile_no': TextInput(attrs={'placeholder': 'Mobile No.'}),
        }


class UploadFileForm(Form):
	file = FileField(required=False)
