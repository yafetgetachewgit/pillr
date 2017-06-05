from .models import Prescription
from rest_framework import serializers


class PrescriptionSerializer(serializers.ModelSerializer):
    drug = serializers.StringRelatedField()

    class Meta:
        model = Prescription
        fields = ('id' ,'drug' , 'start_date', 'doses', 'treatment_duration_days', "total_doses", "time_between_treatments", "the_time_is_in")


