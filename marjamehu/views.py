from django.shortcuts import render
from django.http import Http404, HttpResponse
from .forms import UserLogInForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
	forms,
)



# Create your views here.
def marjamehu(request):
    return render(request, "marjamehu/marjamehu.html", {})


def login(request):
    form = UserLogInForm(request.POST or None)
    title = "LOGIN"
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
    return render(request, "marjamehu/login.html", {"form":form, "title":title})

def registeration(request):
    #if request.method == 'POST'
    form = UserCreationForm
    return render(request, "marjamehu/registeration.html", {})


def logoutView(request):
    return render(request, "form.html", {})
