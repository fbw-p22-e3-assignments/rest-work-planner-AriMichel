# urls.py

from django.urls import include, path
from rest_framework import routers
from .views import EmployeeViewSet, ShiftViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'shifts', ShiftViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
