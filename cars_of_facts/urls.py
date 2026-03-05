from django.urls import path
from cars_of_facts.views import bmw_view , ferrari_view , honda_view

urlpatterns = [
    path('BMW/' , bmw_view ,) ,
    path('Ferrari/' , ferrari_view , ) ,
    path('Honda/' , honda_view),
]