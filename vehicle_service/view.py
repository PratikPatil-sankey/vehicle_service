import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VehicleTypes, EmissionNom, FuelTypes, VehicleDetails
from .serializers import (
    VehicleTypeSerializer, EmissionNomSerializer,
    FuelTypeSerializer, VehicleSerializer
)
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser

from vehicle_service import models
from django.db.models import Q



@csrf_exempt
def create_vehicle_type(request):
    try:
        if request.method == 'POST':
            vehicle_type_data = JSONParser().parse(request)
            serializer = VehicleTypeSerializer(data=vehicle_type_data)

            for field in serializer.fields.keys():
                if serializer.fields[field].required and field not in vehicle_type_data:
                    raise ValueError(f"Missing required field: {field}")

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle type created successfully!!", "data": serializer.data}, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=400)


@csrf_exempt
def get_all_vehicle_type_list(request):
    try:
        vehicle_types = VehicleTypes.objects.all()
        serializer = VehicleTypeSerializer(vehicle_types, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def read_vehicle_type(request, pk):
    try:
        vehicle_type = VehicleTypes.objects.get(pk=pk)
        serializer = VehicleTypeSerializer(vehicle_type)
        return JsonResponse(serializer.data)
    except VehicleTypes.DoesNotExist:
        return JsonResponse({'error': 'Vehicle type not found'}, status=404)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def update_vehicle_type(request, pk):
    try:
    
        vehicle_type = VehicleTypes.objects.get(pk=pk)
    except VehicleTypes.DoesNotExist:
        return JsonResponse({'error': 'Vehicle type not found'}, status=404)

    if request.method == 'PUT':
        try:

            request_data = json.loads(request.body)
            serializer = VehicleTypeSerializer(vehicle_type, data=request_data)
            if serializer.is_valid():
               
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def delete_vehicle_type(request, pk):
    try:
        vehicle = VehicleTypes.objects.get(pk=pk)
        if request.method == 'DELETE':
            vehicle.delete()
            return JsonResponse({"message": "Vehicle deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        print('delete_vehicle()',error)
        return JsonResponse({"message": "Something went wrong"}, status=500)

#---------------------------emmision---------------------------------------------------------------------


@csrf_exempt
def create_emission_nom(request):
    try:
        if request.method == 'POST':
            emission_nom_data = json.loads(request.body)
            serializer = EmissionNomSerializer(data=emission_nom_data)
            
            for field in serializer.fields.keys():
                if serializer.fields[field].required and field not in emission_nom_data:
                    raise ValueError(f"Missing required field: {field}")

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Emission Nom created successfully!!", "data": serializer.data}, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def get_all_ENOM_list(request):
    try:
        emission_noms = EmissionNom.objects.all()
        serializer = EmissionNomSerializer(emission_noms, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def read_emission_nom(request, pk):
    try:
        emission_nom = EmissionNom.objects.get(pk=pk)
        serializer = EmissionNomSerializer(emission_nom)
        return JsonResponse(serializer.data)
    except EmissionNom.DoesNotExist:
        return JsonResponse({'error': 'Emission Nom not found'}, status=404)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def update_emission_nom(request, pk):
    try:
        emission_nom = EmissionNom.objects.get(pk=pk)
    except EmissionNom.DoesNotExist:
        return JsonResponse({'error': 'Emission Nom not found'}, status=404)

    if request.method == 'PUT':
        try:
            request_data = json.loads(request.body)
            serializer = EmissionNomSerializer(emission_nom, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def delete_emission_nom(request, pk):
    try:
        emission_nom = EmissionNom.objects.get(pk=pk)
        if request.method == 'DELETE':
            emission_nom.delete()
            return JsonResponse({"message": "Emission Nom deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
    

@csrf_exempt
def create_fuel(request):
    try:
        if request.method == 'POST':
            fuel_data = json.loads(request.body)
            serializer = FuelTypeSerializer(data=fuel_data)
            
            for field in serializer.fields.keys():
                if serializer.fields[field].required and field not in fuel_data:
                    raise ValueError(f"Missing required field: {field}")

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Fuel type created successfully!!", "data": serializer.data}, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def get_all_fuel_list(request):
    try:
        fuel_types = FuelTypes.objects.all()
        serializer = FuelTypeSerializer(fuel_types, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def read_fuel(request, pk):
    try:
        fuel_type = FuelTypes.objects.get(pk=pk)
        serializer = FuelTypeSerializer(fuel_type)
        return JsonResponse(serializer.data)
    except FuelTypes.DoesNotExist:
        return JsonResponse({'error': 'Fuel type not found'}, status=404)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def update_fuel(request, pk):
    try:
        fuel_type = FuelTypes.objects.get(pk=pk)
    except FuelTypes.DoesNotExist:
        return JsonResponse({'error': 'Fuel type not found'}, status=404)

    if request.method == 'PUT':
        try:
            fuel_data = json.loads(request.body)
            serializer = FuelTypeSerializer(fuel_type, data=fuel_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def delete_fuel(request, pk):
    try:
        fuel = FuelTypes.objects.get(pk=pk)
        if request.method == 'DELETE':
            fuel.delete()
            return JsonResponse({"message": "Fuel type deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        print('delete_fuel()',error)
        return JsonResponse({"message": "Something went wrong"}, status=500)
    
    
@csrf_exempt
def create_vehicle(request):
    try:
        if request.method == 'POST':
            vehicle_data = JSONParser().parse(request)
            
           
            vehicle_type_name = vehicle_data.pop('vehicle_type', None)
            emission_nom_name = vehicle_data.pop('emission_nom', None)
            fuel_type_name = vehicle_data.pop('fuel_type', None)
            
            
            
            emission_nom = EmissionNom.objects.get(emission_nom_name=emission_nom_name)
            fuel_type = FuelTypes.objects.get(fuel_name=fuel_type_name)
            vehicle_type = VehicleTypes.objects.get(vehicle_name=vehicle_type_name)


            vehicle_data['vehicle_type'] = vehicle_type.vehicle_id
            vehicle_data['emission_nom'] = emission_nom.emission_nom_id
            vehicle_data['fuel_type'] = fuel_type.fuel_id
            
            serializer = VehicleSerializer(data=vehicle_data)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle created successfully!!", "data": serializer.data}, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
def get_vehicle(request, pk):
    try:
        vehicle = VehicleDetails.objects.get(pk=pk)
        serializer = VehicleSerializer(vehicle)
        return JsonResponse(serializer.data)
    except VehicleDetails.DoesNotExist:
        return JsonResponse({'error': 'Vehicle not found'}, status=404)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)

@csrf_exempt
def update_vehicle(request, pk):
    try:
        vehicle = VehicleDetails.objects.get(pk=pk)
    except VehicleDetails.DoesNotExist:
        return JsonResponse({'error': 'Vehicle not found'}, status=404)

    if request.method == 'PUT':
        try:
            vehicle_data = JSONParser().parse(request)
            serializer = VehicleSerializer(vehicle, data=vehicle_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def delete_vehicle(request, pk):
    try:
        vehicle = VehicleDetails.objects.get(pk=pk)
        if request.method == 'DELETE':
            vehicle.delete()
            return JsonResponse({"message": "Vehicle deleted successfully"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong"}, status=500)

@csrf_exempt
def get_all_vehicle_list(request):
    try:
        vehicles = VehicleDetails.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
#version
@csrf_exempt
def get_vehicle_by_id(request):
    try:
        user_obj = request.GET.get('user_id')  
        if user_obj:
            vehicle_objects = VehicleDetails.objects.filter(user_id=user_obj, is_deleted=False)
            serializer = VehicleSerializer(vehicle_objects, many=True)
            if serializer.data:
                return JsonResponse({"message": f"Vehicle details for id {user_obj} retrieved successfully!!", "data": serializer.data})
            else:
                return JsonResponse({"message": f"No vehicle details found for date {user_obj}"})
        else:
            return JsonResponse({"message": "Invalid User format."}, status=400)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)   
    


@csrf_exempt
def get_vehicle_details_by_search_v1(request):
    try:
        search_text = request.GET.get('search_text', '')

        vehicle_objects = VehicleDetails.objects.filter(
            Q(vin_no__icontains=search_text) | Q(registration_no__icontains=search_text),
            is_deleted=False
        )

        serializer = VehicleSerializer(vehicle_objects, many=True)

        if serializer.data:
            return JsonResponse({"message": f"Vehicle details matching search text '{search_text}' retrieved successfully!!", "data": serializer.data})
        else:
            return JsonResponse({"message": f"No vehicle details found matching search text '{search_text}'"})
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    


from django.core.paginator import Paginator

    
@csrf_exempt
def get_vehicle_details_by_search_v2(request):
    try:
        search_text = request.GET.get('search_text', '')
        page_number = request.GET.get('page', 1) 
        sort_by = request.GET.get('sort_by', 'vehicle_id')  
       
        vehicle_objects = VehicleDetails.objects.filter(is_deleted=False)

      
        if search_text:
            vehicle_objects = vehicle_objects.filter(
                Q(vin_no__icontains=search_text) | Q(registration_no__icontains=search_text)
            )


        paginator = Paginator(vehicle_objects, 5)  
        page = paginator.get_page(page_number)

       
        if sort_by in ['vehicle_id', 'vin_no', 'registration_no', 'created_at', 'updated_at']:
            vehicle_objects = vehicle_objects.order_by(sort_by)

        serializer = VehicleSerializer(page, many=True)

        if serializer.data:
            return JsonResponse({
                "message": f"Vehicle details matching search text '{search_text}' retrieved successfully!!",
                "data": serializer.data,
                "total_pages": paginator.num_pages,
                "current_page": page.number,
                "has_next_page": page.has_next(),
                "has_previous_page": page.has_previous(),
            })
        else:
            return JsonResponse({"message": f"No vehicle details found matching search text '{search_text}'"})
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)