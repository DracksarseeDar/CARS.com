from django.urls import path
from . import views

app_name = 'drivers'

urlpatterns = [
    path('create_driver/', views.DriverCreateView.as_view(), name='create_driver'),
    path('driver_list/', views.DriverListView.as_view(), name='driver_list'),
    path('driver_list/<int:id>/update/', views.DriverUpdateView.as_view(), name='update_driver'),
    path('driver_list/<int:id>/delete/', views.DriverDeleteView.as_view(), name='delete_driver'),
]