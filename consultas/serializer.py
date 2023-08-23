from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        # fields = ('id', 'name', 'tipe_donation', 'tipe_user', 'donation')
        fields = '__all__'