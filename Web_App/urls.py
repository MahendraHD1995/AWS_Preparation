from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about_me/', views.about_me, name="about_me"), 
    path('aws_test/',views.aws_test, name="aws_test"),
    path('aws_start_test/',views.aws_start_test,name="aws_start_test"),
]