
from .models import Patient
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.forms import HiddenInput




class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Enter password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)

    class Meta:
	    model = User
	    fields = ("username", "email", "password1", "password2")

    help_text = {
        "username": None,
    }

class PatientForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(PatientForm, self).__init__(*args,**kwargs)
        self.fields['user'].widget=HiddenInput()
    class Meta:
        model = Patient
        fields = ("user","name","date","time","department","doctor","phone","message")
        widgets = {
            'date': forms.SelectDateWidget(),
            'message': forms.Textarea(attrs={'style': 'height: 150px;width:400px'})



        }


