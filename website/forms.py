from django.forms import ModelForm, HiddenInput
from website.models import Assignment

class AssignmentForm(ModelForm):
	class Meta:
		model =  Assignment
		exclude = ['user']
