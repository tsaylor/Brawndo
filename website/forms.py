from django.forms import ModelForm
from website.models import Assignment

class AssignmentForm(ModelForm):
	class Meta:
		model =  Assignment
		exclude = ['task']
