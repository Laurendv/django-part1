from django.urls import path
from . import views

#Url conf module
urlpatterns = [
    path('hello/', views.say_hello),
]