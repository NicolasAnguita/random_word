from django.urls import path     
from . import views
urlpatterns = [
    path('random_world', views.index),	   
]