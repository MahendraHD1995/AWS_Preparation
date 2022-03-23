
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

from .forms import AWS_Topics_Selected,InputForm


def about_me(request):
    return render(request,'web_app/about_me.html')

def aws_test(request):  
   
    
    context = {
        "data" : ['SQS','Cloud Trail','EC2','Lambda','IAM','SNS','Cloud Watch','VPC'],
    }
    print("Mahendra")
    request.GET.getlist('Project')
    
    if request.POST:
        print("Inside post :")
        print(request.GET.getlist())
    return render(request,'web_app/aws_tests.html',context)

# def aws_start_test(request):
#     return render(request,'web_app/aws_start_test.html')

def aws_start_test(request):
    
    try:
        if request.method=="POST":
            for q in request.POST.items():
                print(q)
    except:
        pass

    # a =EC2(QUESTION='What does the following command do with respect to the Amazon EC2 security groups? ec2-create-group CreateSecurityGroup',
    # OPTION_A='Groups the user created security groups into a new group for easy access.', 
    # OPTION_B='Creates a new security group for use with your account.',
    # OPTION_C='Creates a new group inside the security group.',
    # OPTION_D='Creates a new rule inside the security group.',
    # ANSWER='OPTION_B' )
    # a.save()
    


    return render(request,'web_app/aws_start_test.html',{'aws_questions':EC2.objects.all()})

@login_required(login_url='login')
def home(request):
	return render(request, 'web_app/home.html')

def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)