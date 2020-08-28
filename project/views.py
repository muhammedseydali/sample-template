from django.shortcuts import render
from django.template import loader  


# Create your views here.
def index(request):
	return render(request,'indexx.html')

def ali(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def destinations(request):
	return render(request,'destinations.html')

def elements(request):
	return render(request,'elements.html')

def news(request):
	return render(request,'news.html')
