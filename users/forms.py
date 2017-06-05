from django import forms
from django.contrib.auth.models import User
from .models import Patient


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UserInfoForm(forms.ModelForm):

	class Meta:
		model = Patient
		fields = ('height', 'weight', 'doctors', 'region')


class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password')
