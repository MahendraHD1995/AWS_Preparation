from ast import Lambda
from django import forms
  
# creating a form 


class AWS_Topics_Selected(forms.Form):
    SQS = forms.BooleanField(required = False)
    SNS = forms.BooleanField(required = False)
    Lambda = forms.BooleanField(required = False)
    Cloud_Watch = forms.BooleanField(required = False)
    Cloud_Trail = forms.BooleanField(required = False)
    IAM = forms.BooleanField(required = False)
    VPC = forms.BooleanField(required = False)
    EC2 = forms.BooleanField(required = False)


# creating a form
class InputForm(forms.Form):

	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number"
					)
	password = forms.CharField(widget = forms.PasswordInput())
