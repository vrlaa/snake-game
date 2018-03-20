from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def marjamehu(request):

	return render(request, "marjamehu/marjamehu.html", {})