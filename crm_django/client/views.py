from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from lead.models import Lead
from team.models import Team

from .models import Client, Note
from .serializers import ClientSerializer, NoteSerializer


class ClientPagination(PageNumberPagination):
    page_size = 10
    
class ClientViewSet(viewsets.ViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter)
    search_fields = ('name', 'contact_person')
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first() # m2one
        serializer.sve(team=team, created_by=self.request.user)
        
    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)
    
    