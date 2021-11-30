from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Lead
from .serializers import LeadSerializer


class LeasViewSet(viewsets.ModelViewSet):
    """ return logged in user leads """
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
    
    def get_queryset(self):
        """ filter logged in user leads """
        return self.queryset.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
        
@api_view(['POST'])
def delete_lead(request, lead_id):
    lead = Lead.objects.filter(pk=lead_id)
    lead.delete()
    return Response({'message': 'The lead was deleted'})