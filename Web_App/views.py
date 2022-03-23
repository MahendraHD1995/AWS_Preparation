from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from matplotlib.style import context


# Create your views here.
from .models import *
# Create your views here.

from .forms import AWS_Topics_Selected, ExampleForm, InputForm


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

    import psycopg2

    try:
            connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="aws_preparation")
            cursor = connection.cursor()
            postgreSQL_select_Query = "select * from EC2"

            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from mobile table using cursor.fetchall")
            mobile_records = cursor.fetchall()
            

            print("Print each row and it's columns values")
            for row in mobile_records:
                print("Id = ", row[0], )
                print("Question = ", row[1])
                print("A  = ", row[2])
                print("B  = ", row[3])
                print("C  = ", row[4])
                print("D  = ", row[5])
                print("E  = ", row[6])
                print("Answer  = ", row[7])

    except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

    finally:
         # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    print("outside loop : \n")
    print(mobile_records)
    return render(request,'web_app/aws_start_test.html',{'aws_questions':mobile_records})

@login_required(login_url='login')
def home(request):
	return render(request, 'web_app/home.html')

def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)