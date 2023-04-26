from django.urls import path
from . import views
urlpatterns = [
    path('cropprediction/', views.prediction_page),
    path('', views.home),
]