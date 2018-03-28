from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm




# Create your views here.
def marjamehu(request):
    return render(request, "marjamehu/marjamehu.html", {})

def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)
