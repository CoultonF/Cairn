from trip_reports.models import TripReport
from rest_framework import viewsets, permissions
from .serializers import TripReportSerializer
from rest_framework import filters

class TripReportViewSet(viewsets.ModelViewSet):
    queryset = TripReport.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TripReportSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['trail']