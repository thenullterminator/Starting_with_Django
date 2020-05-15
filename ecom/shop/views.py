from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
      return render(request,'shop/index.html')

def contact(request):
      return HttpResponse("Contact")

def about(request):
      return HttpResponse("about")

def tracker(request):
      return HttpResponse("tracker")

def search(request):
      return HttpResponse("search")

def checkout(request):
      return HttpResponse("checkout")

def productview(request):
      return HttpResponse("product view")