from rest_framework import serializers
from .models import VehicleTypes, EmissionNom, FuelTypes, VehicleDetails


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTypes
        fields = '__all__'


class EmissionNomSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionNom
        fields = '__all__'


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelTypes
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDetails
        fields = '__all__'
