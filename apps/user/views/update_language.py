from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models.base import User
from user.serializers.update_language import UpdateLanguageSerializer


class UpdateLanguageView(APIView):

    def put(self,request):
        serializer = UpdateLanguageSerializer(instance=request.user,data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.language = serializer.validated_data['language']
        user.save()
        return Response({"detail":"language has been updated successfully!"},status=status.HTTP_202_ACCEPTED)
