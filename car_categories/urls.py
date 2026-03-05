from django.urls import path
from car_categories.views import car_list_view, car_detail_view

urlpatterns = [
    path('cars_list/', car_list_view),
    path('cars_list/<int:id>/', car_detail_view),
]