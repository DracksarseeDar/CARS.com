from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('car_list/<int:id>/', views.CarDetailView.as_view(), name='car_detail'),
]