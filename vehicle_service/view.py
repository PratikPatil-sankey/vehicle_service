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


@csrf_exempt
def create_vehicle_type(request):
    try:
        if request.method == 'POST':
            vehicle_type = JSONParser().parse(request)
            serializer = VehicleTypeSerializer(data=vehicle_type)
            
            if serializer.is_valid():
                
                serializer.save()
                return JsonResponse({"message": "Vehicle type created successfully!!", "data": serializer.data}, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


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