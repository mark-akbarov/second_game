# Rest-Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Project
from user.serializers.me import UserSerializer


class UserMeAPIVIew(APIView):
    serializers_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        context = {'request': request}
        serializer = self.serializers_class(request.user, context=context)
        return Response(data=serializer.data)
