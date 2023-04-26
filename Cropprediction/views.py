from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Home Page
def home(request):
    return HttpResponse("Home")

def prediction_page(request):
    return HttpResponse("HIII ")