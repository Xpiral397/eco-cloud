from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_helo(request):
    return HttpResponse('say_hello')
    
