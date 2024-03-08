from django.shortcuts import render
from django.http import HttpResponse

def ali(request) :
    return HttpResponse("hi ali")

 
def welcome(request) :
    return HttpResponse("welcome to this page ")

def yourname(reauest,name):
    return HttpResponse(f"hi {name}")

def home(request):
    return render(request,"home/index.html")

def gholi(request)  :
    return HttpResponse("hello gholi")
   