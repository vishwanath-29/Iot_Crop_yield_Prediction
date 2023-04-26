from django.shortcuts import render
from django.http import HttpResponse
from .models import Valuesfromsensor
import pytz
import random
import pickle
import pandas as pd
# Home Page
def home(request):
    return HttpResponse("Home")

def yield_prediction(temperature,humidity,pH,moisture,rainfall):
    model = pickle.load(open('/home/vishwa/Work/Programming/VsCode/Web/Django/IoT-Wheat-yield-prediction/wheat_yield_prediction_model.pkl', 'rb'))
    dataset_columns = ['Temperature','Humidity','Moisture','Rainfall','pH']
    data = {}
    data[dataset_columns[0]]=temperature
    data[dataset_columns[1]]=humidity
    data[dataset_columns[2]]=moisture
    data[dataset_columns[3]]=rainfall
    data[dataset_columns[4]]=pH

    # Convert dictionary to dataframe
    df = pd.DataFrame(data, columns=dataset_columns,index=[0])
    predictions = model.predict(df)
    print("Prediction:",predictions[0])
    return predictions[0]

def prediction_page(request):
    sensor_values = Valuesfromsensor.objects.last()
    ist_time = pytz.timezone('Asia/Kolkata')
    temperature=sensor_values.temperature
    humidity=sensor_values.humidity
    pH=sensor_values.ph
    moisture=sensor_values.moisture
    rainfall=round(random.uniform(75,100), 2)

    valuedatetime=sensor_values.eventprocessedutctime
    valuedatetime = valuedatetime.astimezone(ist_time)
    valuetime = valuedatetime.strftime('%H:%M:%S')
    valuedate=valuedatetime.date()
    
    print(temperature," ",humidity," ",pH," ",moisture," ",valuetime," ",valuedate)
    yield_predicted=yield_prediction(temperature,humidity,pH,moisture,rainfall)
    return HttpResponse(yield_predicted)