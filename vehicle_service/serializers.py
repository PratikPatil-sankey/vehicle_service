from rest_framework import serializers
from .models import VehicleTypes, EmissionNom, FuelTypes, VehicleDetails


class VehicleTypeSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle_name'].required = True 

    class Meta:
        model = VehicleTypes
        fields = ('vehicle_name',)

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
