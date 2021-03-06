from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm,LoginForm


def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['form'] = form

	else:
		form = RegistrationForm()
		context['form'] = form
	return render(request, 'registration/register.html', context)

def LogoutView(request): 
	logout(request)
	return redirect('home')

def LoginVeiw(request):
	context = {}

	user = request.user
	# if the user is login in already

	if user.is_authenticated:
		return redirect("home")
	 	# if we want to submit the form
	# if request.POST:
	# 	if not user.is_active:
	# 		return redirect("blocked")
	if request.POST:
	 	form = LoginForm(request.POST)
	 	if form.is_valid():
	 		email = request.POST['email']
	 		password = request.POST['password']
	 		user = authenticate(email=email, password=password)

	 		if user:
	 			login(request, user)
	 			if not user.is_blocked:
	 				return redirect ("blocked")
	 			return redirect("home")
	# show the form for the first time
	else:
	 	form = LoginForm()

	context['form'] = form
	return render(request, 'registration/login.html', context)

def AdminLoginView(request):
		logout(request)
		context = {}
		user = request.user
		# if the user is login in already

		if user.is_authenticated:
		 	return redirect("home")
		 	# if we want to submit the form
		if request.POST:
		 	form = LoginForm(request.POST)
		 	if form.is_valid():
		 		email = request.POST['email']
		 		password = request.POST['password']
		 		user = authenticate(email=email, password=password)

		 		if user:
		 			login(request, user)
		 			return redirect("home")
		# show the form for the first time
		else:
		 	form = LoginForm()

		context['form'] = form
		return render(request, 'registration/admin_login.html', context)

def EditView(request):

	if not request.user.is_authenticated:
		return redirect("login")

	context = {}

	if request.POST:
		form = RegistrationForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
	else:
		form = RegistrationForm(
				initial= {
					"email": request.user.email,
					"username": request.user.username,
				}
			)
	context['account_form'] = form
	return render(request, "registration/edit.html", context)

def blockedView(request):
	return render(request, "registration/blocked.html", {})