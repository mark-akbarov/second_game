# Rest-Framework
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Project
from user.serializers.update import UserUpdateSerializer
from user.services.update import user_update


class UpdateUserAPIView(APIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = self.serializer_class(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        return user_update(user=user, **serializer.validated_data)
