# I created this file....
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
      return HttpResponse("<u>Home Page</u>")

def Text(request):
      return render(request,'index.html')

def recieve(request):
      t=request.GET.get('text','Nothing')
      print(t)
      return HttpResponse("<u>" +t+"</u>")