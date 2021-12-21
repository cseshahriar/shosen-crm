from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    NEW = 'new'
    CONTACTED = 'contacted'
    INPROGRESS = 'inprogress'
    LOST = 'lost'
    WON = 'won'
    
    STATUS_CHOICES = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (INPROGRESS, 'Inprogress'),
        (LOST, 'Lost'),
        (WON, 'Won')
    )
    
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    PRIORITY_CHOICES = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    
    company = models.CharField(max_length=355)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    website = models.URLField(max_length=255, null=True, blank=True)
    confidence = models.IntegerField(null=True, blank=True)
    estimated_value = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=25, choices=STATUS_CHOICES, default=NEW
    )
    priority = models.CharField(
        max_length=25, choices=PRIORITY_CHOICES, default=MEDIUM
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="assignedleads",
        null=True, blank=True
    )
    created_by = models.ForeignKey(
        User, related_name="leads", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.contact_person