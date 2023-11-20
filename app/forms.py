from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from app.models import Employee 

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }
   

class LoginForm(AuthenticationForm):
    username = UsernameField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))


class AddForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','email','address','profileimg']
        labels = {'name':'Name','email':'Email','address':'Address','profileimg':'Image'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
        }


