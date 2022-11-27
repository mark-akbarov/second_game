# Rest-Framework
from rest_framework import serializers

# Project
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'birthday',
            'about',
            'is_new',
            'score',
        ]


class UserMeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
        ]


class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['score', 'winner']