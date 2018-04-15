from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm

from crispy_forms.helper import FormHelper

from marjamehu.models import CustomUser


# Form for registeration
#class RegistrationForm(forms.ModelForm):
class RegistrationForm(UserCreationForm):
    #username = forms.CharField(label='Username')
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Repeat the password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        #model = User
        #fields = ('username', 'developer',)
        #fields = UserCreationForm.Meta.fields# + ('developer',)
        fields = UserCreationForm.Meta.fields + ('developer',)

    # Check that the two passwords exist and match
    # def check_passwords(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 != password2 and password1 and password2:
    #         # Raise ValidationError
    #         raise forms.ValidationError("Passwords do NOT match")
    #     return password1
    #
    # #Save password
    # def save(self, commit=True):
    #     user = super().save(commit=True)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget = forms.PasswordInput)
