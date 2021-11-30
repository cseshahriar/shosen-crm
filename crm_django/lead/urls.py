from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeasViewSet, delete_lead


router = DefaultRouter()
router.register('leads', LeasViewSet, basename='leads')

urlpatterns = [
    path('leads/delete_lead/<int:lead_id>/', delete_lead, name='delete_lead'),
    path('', include(router.urls)),
]