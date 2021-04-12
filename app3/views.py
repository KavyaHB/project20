from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def display(request,input):
    return HttpResponse(f'<h1>the input is {input}</h1>')