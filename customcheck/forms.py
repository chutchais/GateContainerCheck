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


class RejectForm(forms.Form):
    container = forms.CharField(label='Container/Truck ID', max_length=20,
    #     validators=[
    #     RegexValidator(
    #         regex='^[A-Z]{4}[0-9]{7}$',
    #         message='Container is wrong format (should be like : SEGU4598414)',
    #         code='invalid_username'
    #     ),
    # ]
    )

    no_shore = forms.BooleanField(label ='No Shore')
    no_paid = forms.BooleanField(label ='ติดจ่ายตังค์')
    no_customs = forms.BooleanField(label ='ติด Custom')
    no_vgm = forms.BooleanField(label ='No VGM')
    late_gate = forms.BooleanField(label ='Late Gate')
    other = forms.CharField(label ='อื่นๆ',max_length=100)
    comment = forms.CharField(label='Comment',widget=forms.Textarea,required=False)


    # container_no = models.CharField(max_length=50)
    # description = models.TextField(blank=True, null=True)
    # no_shore = models.BooleanField(verbose_name ='No Shore')
    # no_paid = models.BooleanField(verbose_name ='ติดจ่ายตังค์')
    # no_customs = models.BooleanField(verbose_name ='ติด Custom')
    # no_vgm = models.BooleanField(verbose_name ='No VGM')
    # late_gate = models.BooleanField(verbose_name ='Late Gate')
    # other = models.CharField(verbose_name ='อื่นๆ',max_length=100)
    # created_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
    # user = models.ForeignKey('auth.User',blank=True,null=True)

#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))