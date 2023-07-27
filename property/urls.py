from django.urls import path
from . import views

urlpatterns =[
    path('properties/', views.ProperyList.as_view(), name='properties'),
]