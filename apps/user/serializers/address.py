from rest_framework import serializers
from user.models.address import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = [
            'id',
            'city',
            'region',
            'street_home',
            'building_number',
            'building_floor',
            'phone_number',
            'is_default'
        ]
