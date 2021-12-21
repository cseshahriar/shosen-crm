from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Lead
from .serializers import LeadSerializer
from team.models import Team


class LeasViewSet(viewsets.ModelViewSet):
    """ return logged in user leads """
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
    def get_queryset(self):
        """ filter logged in user leads """
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team,created_by=self.request.user)
        
    def perform_update(self, serializer):
        obj = self.get_object()
        member_id = self.request.data['assigned_to']
        
        if member_id:
            try:
                user = User.objects.get(pk=member_id)
                serializer.save(assigned_to=user)
            except User.DoesNotExist:
                print("User does not exists.")
                return Response({'error': 'User does not exist'}, 400)
        else:
            serializer.save()
                
        
        
@api_view(['POST'])
def delete_lead(request, lead_id):
    lead = Lead.objects.filter(pk=lead_id)
    lead.delete()
    return Response({'message': 'The lead was deleted'})