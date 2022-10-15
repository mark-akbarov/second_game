# Rest-Framework
from rest_framework import serializers

# Model
from user.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'smartphone_type'
        ]
