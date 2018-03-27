from django import forms

class UserLogInForm(forms.Form):
    username = forms.CharField():
    password = forms.CharField(widget=forms.PasswordInput)
