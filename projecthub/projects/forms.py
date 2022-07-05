from django.forms import ModelForm
from .models import Project

from django import forms # new
from django.contrib.auth.forms import UserCreationForm # new
from django.contrib.auth.models import User # new


class ProjectsForm(ModelForm):
    class Meta:
        model = Project
         # exclude = ['project_priority_sl']
        fields = '__all__'
        #new
# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user