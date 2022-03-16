from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


# Create your views here.
from .models import *
# Create your views here.


def about_me(request):
    return render(request,'web_app/about_me.html')

def aws_test(request):
    return render(request,'web_app/aws_tests.html')

def aws_start_test(request):
    return render(request,'web_app/aws_start_test.html')

@login_required(login_url='login')
def home(request):
	return render(request, 'web_app/home.html')