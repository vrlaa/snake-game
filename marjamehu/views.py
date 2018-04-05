from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login




# Create your views here.
def marjamehu(request):
    return render(request, "marjamehu/marjamehu.html", {})

def home(request):
    return render(request, "marjamehu/base.html", {})

def peli(request):
    return render(request, "marjamehu/peli.html", {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #Create user
            form.save()
            # Get data from the passed form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Authenticate the user
            user = authenticate(username=username, password=password)
            # Log the user in
            login(request, user)
            # Return to home page
            return redirect ('marjamehu')

    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)
