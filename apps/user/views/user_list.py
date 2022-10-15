# Rest-Framework
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters

# Project
from user.models import User
from user.serializers.me import UserMeSerializer


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserMeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']

    def get_queryset(self):
        user_list = User.objects.filter(is_superuser=False, is_staff=False)
        return user_list
