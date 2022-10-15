# Rest-Framework
from rest_framework import serializers

# Project
from user.models import User


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'birthday',
            'smartphone_type',
            'about',
            'is_new',
        ]


class UserMeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
        ]
