from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome to this home page")


def ali(request):
    return HttpResponse('hello ali')

def name(request,name):
    return HttpResponse(f'hello {name}')
