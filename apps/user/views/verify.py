# Rest-Framework
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Project
from user.serializers.verify import UserVerifySerializer, ReSendVerifyUserSerializer
from user.services.verify import check_verify_signup_code, re_send_verify_user_code


class VerifyUserAPIView(APIView):
    serializer_class = UserVerifySerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return check_verify_signup_code(**serializer.validated_data)


class ReSendVerifyUserAPIView(APIView):
    serializer_class = ReSendVerifyUserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return re_send_verify_user_code(**serializer.validated_data)
