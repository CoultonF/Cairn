from rest_framework import routers
from .api import TripReportViewSet

router = routers.DefaultRouter()
router.register('api/trip_reports', TripReportViewSet, 'trip_reports')

urlpatterns = router.urls