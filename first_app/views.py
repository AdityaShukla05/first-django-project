from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")
def homee(request):
    return HttpResponse("Welcome to home page!")
def scaler(request):
    return HttpResponse("Welcome to scaler page!")
def namee(request, name):
    return HttpResponse(f"Welcome {name}!")
def about(request):
    return HttpResponse("""
        <h1> About Me </h1>
        <p> Hello Iam Aditya Shukla from Edge Nov20 SuperX Batch.
        Iam feeling luckly. 
        </p>
    """)