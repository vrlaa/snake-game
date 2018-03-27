from django.shortcuts import render
from django.http import Http404, HttpResponse
from .forms import UserLogInForm
form django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
# Create your views here.
def marjamehu(request):

	return render(request, "marjamehu/marjamehu.html", {})
def loginView(request):
	form = UserLogInForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")

	return render(request, "form.html",{})

def registerView(request):
	return render(request, "form.html",{})

def logoutView(request):
	return render(request,"form.html",{})
