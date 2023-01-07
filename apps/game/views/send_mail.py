from rest_framework.response import Response
from rest_framework.views import APIView
from game.tasks import send_feedback_mail
from game.serializers.send_mail import SendEmailSerializer


class SendEmailView(APIView):
    serializer_class = SendEmailSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_feedback_mail.delay(**serializer.validated_data)
        return Response({"detail":"success"})