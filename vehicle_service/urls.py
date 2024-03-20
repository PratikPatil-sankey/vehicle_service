"""
URL configuration for vehicle_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import view
 
urlpatterns = [ 
               
               
    path('vehicle_type/create/', view.create_vehicle_type, name='create_vehicle_type'),
    path('vehicle_type/get_all',view.get_all_vehicle_type_list,name='get_all_vehicle_type_list'),
    path('vehicle_type/<int:pk>/', view.read_vehicle_type, name='read_vehicle_type'),
    path('vehicle_type/update/<int:pk>/', view.update_vehicle_type, name='update_vehicle_type'),
    path('vehicle_type/delete/<int:pk>/', view.delete_vehicle_type, name='delete_vehicle_type'),


    # path('vehicle/create/', view.create_vehicle, name='create_vehicle'),
    # path('vehicle/<int:pk>', view.get_vehicle, name='read_vehicle'),
    # path('vehicle/update<int:pk>/', view.update_vehicle, name='update_vehicle'),
    # path('vehicle/delete/<int:pk>/', view.delete_vehicle, name='delete_vehicle'),
    # path('vehicle/get_all', view.get_all_vehicle_list, name='get_all_vehicle_list'),

    path('emission_nom/create/', view.create_emission_nom, name='create_emission_nom'),
    path('emission_nom/get_all',view.get_all_ENOM_list,name='get_all_ENOM_list'),
    path('emission_nom/<int:pk>/', view.read_emission_nom, name='read_emission_nom'),
    path('emission_nom/update/<int:pk>/', view.update_emission_nom, name='update_emission_nom'),
    path('emission_nom/delete/<int:pk>/', view.delete_emission_nom, name='delete_emission_nom'),

    path('fuel_type/create_fuel/', view.create_fuel, name='create_fuel_type'),
    path('fuel_type/get_all/', view.get_all_fuel_list, name='get_all_fuel_list'),
    path('fuel_type/<int:pk>/', view.read_fuel, name='read_fuel'),
    path('fuel_type/update/<int:pk>/', view.update_fuel, name='update_fuel'),
    path('fuel_type/delete/<int:pk>/', view.delete_fuel, name='delete_fuel'),
   
    path('vehicle/create/', view.create_vehicle, name='create_vehicle'),
    path('vehicle/<int:pk>', view.get_vehicle, name='read_vehicle'),
    path('vehicle/update/<int:pk>/', view.update_vehicle, name='update_vehicle'),
    path('vehicle/delete/<int:pk>/', view.delete_vehicle, name='delete_vehicle'),
    path('vehicle/get_all', view.get_all_vehicle_list, name='get_all_vehicle_list'),
    
    path('api/vehicle_details/get_vehicle_by_id', view.get_vehicle_by_id, name='get_vehicle_by_id'),
    path('api/vehicle_details/get_vehicle_details_by_search_v1/', view.get_vehicle_details_by_search_v1, name='get_vehicle_details_by_search_v1/'),
    path('api/vehicle_details/get_vehicle_details_by_search_v2/', view.get_vehicle_details_by_search_v2, name='get_vehicle_details_by_search_v2/'),
  
]