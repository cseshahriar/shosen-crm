from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeasViewSet

router = DefaultRouter()
router.register('leads', LeasViewSet, basename='leads')

urlpatterns = [
    path('', include(router.urls)),
]