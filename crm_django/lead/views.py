from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import Lead
from .serializers import LeadSerializer


class LeasViewSet(viewsets.ModelViewSet):
    """ return logged in user leads """
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
    
    def get_queryset(self):
        """ filter logged in user leads """
        return self.queryset.filter(created_by=self.request.user)