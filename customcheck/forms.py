from django import forms
from django.core.validators import RegexValidator

class ContainerForm(forms.Form):
    container = forms.CharField(label='Container Number', max_length=20,
    	validators=[
        RegexValidator(
            regex='^[A-Z]{4}[0-9]{7}$',
            message='Container is wrong format (should be like : SEGU4598414)',
            code='invalid_username'
        ),
    ])
    comment = forms.CharField(label='Comment',widget=forms.Textarea,required=False)



#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))