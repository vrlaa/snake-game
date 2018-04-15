from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, get_user_model
from django import forms


from marjamehu.forms import (
    LoginForm,
    RegistrationForm
)


# Create your views here.
def marjamehu(request):
    return render(request, "marjamehu/marjamehu.html", {})

def home(request):
    return render(request, "marjamehu/base.html", {})

def peli(request):
    return render(request, "marjamehu/peli.html", {})

def loginPage(request):
    # form = LoginForm(request.POST, error_class=forms.ValidationError)
    form = LoginForm(request.POST)
    title = "Login"
    context = {"form":form, "title":title}
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("User does not exist")
        else:
            raise forms.ValidationError("Somethings shitty")
    return render(request, "marjamehu/form.html", context)


def registerPage(request):
    if request.method == 'POST':
        #form2 = RegistrationForm(request.POST)
        form = RegistrationForm(request.POST,  error_class=forms.ValidationError)
        if form.is_valid():
            # Create user
            form.save()
            # Get data from the passed form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Authenticate the user
            user = authenticate(username=username, password=password)
            # Log the user in
            login(request, user)
            # Return to home page
            return redirect('home')
            #else:
            #    raise ValidationError("Somethings shitty")
    else:
        title = "Register"
        form = RegistrationForm()
        context = {'form':form, "title":title}
    return render(request, 'marjamehu/form.html', context)
