from rest_framework import serializers
from trip_reports.models import TripReport


class TripReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripReport
        fields = '__all__'