from django.shortcuts import render
from .models import ExtendedUser
# Create your views here.

def home(request):
	users = ExtendedUser.objects.all()
	context  ={
	'users':users

	}
	return render(request,'Accounts/home.html',context)


