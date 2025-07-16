from django.urls import path, include
from .views import CompanyViewSet,EmployeeViewSet
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r"Companies", CompanyViewSet)
router.register(r"Employees", EmployeeViewSet) 

urlpatterns = [
    path('', include(router.urls))
]
