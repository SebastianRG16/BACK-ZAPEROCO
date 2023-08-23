from django.shortcuts import render
from rest_framework import viewsets
from .serializer import DonationSerializer
from .models import Donation

# Create your views here.
class DonationView(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()