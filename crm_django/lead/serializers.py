from django.db.models import fields
from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.Modelserializer):
    
    class Meta:
        model = Lead
        fields = (
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'estimated_value',
            'status',
            'priority',
            'created_by',
            'created',
            'updated'
        )