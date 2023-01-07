from rest_framework import serializers


class SendEmailSerializer(serializers.Serializer):
    recipient = serializers.EmailField()
    message = serializers.CharField()