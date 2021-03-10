from django.urls import path

from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls'))
]