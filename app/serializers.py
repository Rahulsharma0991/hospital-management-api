from rest_framework import serializers
from .models import Patient,Doctor,Appointment

# Patient_Seralizers
class Patient_serializers(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'
# # Doctor_Seralizers
class Doctor_serializers(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

# Appointment_serailazers

class Appointment_serializers(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'

        