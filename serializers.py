
from rest_framework import serializers
from .models import Employee, Shift

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    shifts = ShiftSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'