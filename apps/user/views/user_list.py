# Rest-Framework
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters

# Project
from user.models import User
from user.serializers.me import UserSerializer


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']

    def get_queryset(self):
        user_list = User.objects.filter(is_superuser=False, is_staff=False)
        return user_list
