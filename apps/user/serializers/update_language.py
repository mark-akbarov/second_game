from rest_framework import serializers
from user.models.base import User


class UpdateLanguageSerializer(serializers.Serializer):
    language = serializers.CharField()
