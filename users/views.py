from django.shortcuts import render
from .forms import UserForm, UserInfoForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token


def register(request):

	registered = False

	if request.method == 'POST':

		user_form = UserForm(data=request.POST)
		info_form = UserInfoForm(data=request.POST)

		if user_form.is_valid() and info_form.is_valid():

			user = user_form.save()

			user.set_password(user.password)
			user.save()

			default_group = Group.objects.get(name="patients")
			default_group.user_set.add(user)
			info = info_form.save(commit=False)
			info.user = user
			info.save()
			Token.objects.get_or_create(user=user)
			registered = True
		else:
			print user_form.errors, info_form.errors

	else:
		user_form = UserForm()
		info_form = UserInfoForm()

	return render(request, 'users/register.html', {'user_form': user_form, 'info_form': info_form, 'registered': registered})


def user_login(request):

	if request.method == 'POST':		

		username = request.POST.get('username')
		password = request.POST.get('password')		
		user = authenticate(username=username, password=password)

		if user:

			if user.is_active:
				login(request, user)
				if user.groups.filter(name="pharma"):
					return render(request, 'dashboard/pharma.html')
				else:
					return HttpResponseRedirect('/')
			else:
				login_form = LoginForm(data=request.POST)
				message = "Your account seems to be disabled."
				return render(request, 'users/login.html', {'login_form': login_form, 'message': message})
		else:
			login_form = LoginForm(data=request.POST)
			message = "The information you've entered seems to be inaccurate, please try again."
			return render(request, 'users/login.html', {'login_form': login_form, 'message': message})

	else:
		login_form = LoginForm()
		return render(request, 'users/login.html', {'login_form': login_form})

def user_logout(request):
	logout(request)

	return HttpResponseRedirect("/")
