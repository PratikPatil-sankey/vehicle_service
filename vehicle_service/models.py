from django.db import models
 

 
class VehicleTypes(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'vehicle_types' 

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
 
class EmissionNom(models.Model):
    emission_nom_id = models.AutoField(primary_key=True)
    emission_nom_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'emission_nom'  # Set the table name to 'emission_nom'

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
        
class FuelTypes(models.Model):
    fuel_id = models.AutoField(primary_key=True)
    fuel_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'fuel_types' 

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
class VehicleDetails(models.Model):
 
    vehicle_id = models.IntegerField(primary_key=True)
    vin_no = models.CharField(max_length=17, unique=True)
    registration_no = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=50)
    user_id = models.CharField(max_length=16)

    fuel_type = models.ForeignKey(FuelTypes, on_delete=models.CASCADE)
    vehicle_type = models.ForeignKey(VehicleTypes, on_delete=models.CASCADE)
    emission_nom = models.ForeignKey(EmissionNom, on_delete=models.CASCADE)
 
    model_name = models.CharField(max_length=20)
    engine_no = models.CharField(max_length=15)
    making_date = models.DateField()
    is_onboard = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'vehicle_details' 

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()


