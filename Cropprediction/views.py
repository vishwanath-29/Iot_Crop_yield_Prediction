from django.shortcuts import render
from django.http import HttpResponse
from .models import Valuesfromsensor
import pytz
# Create your views here.

# Home Page
def home(request):
    return HttpResponse("Home")

def prediction_page(request):
    sensor_values = Valuesfromsensor.objects.last()
    ist_time = pytz.timezone('Asia/Kolkata')
    valuedatetime=sensor_values.eventprocessedutctime
    valuedatetime = valuedatetime.astimezone(ist_time)
    valuetime = valuedatetime.strftime('%H:%M:%S')
    valuedate=valuedatetime.date()
    print(sensor_values.temperature," ",valuetime," ",valuedate)
    return HttpResponse("HII")