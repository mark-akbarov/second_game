# Django
from django.urls import path, include

# Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from .views.forgot_password import SendForgotPasswordAPIView, CheckForgotPasswordCodeView, ForgotPasswordView
from .views.login import LoginAPIView
from .views.me import UserMeAPIVIew
from .views.signup import SignupView
from .views.update import UpdateUserAPIView
from .views.user_list import UserListAPIView
from .views.verify import ReSendVerifyUserAPIView
from .views.verify import VerifyUserAPIView
from .views.address import AddressViewSet
from .views.update_language import UpdateLanguageView
from .views.user_rating import UserRatingListAPIView, UserScoreRatingAPIView, Leaderboard, LeaderboardWinner

router = DefaultRouter()
router.register('address', AddressViewSet, basename='address')


urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', SignupView.as_view()),
    path('me/', UserMeAPIVIew.as_view()),
    path('update/', UpdateUserAPIView.as_view()),
    path('user_list/', UserListAPIView.as_view()),
    path('verify_user/', VerifyUserAPIView.as_view()),
    path('resend_verify_code/', ReSendVerifyUserAPIView.as_view()),
    path('send_forgot_password/', SendForgotPasswordAPIView.as_view()),
    path('check_forgot_password/', CheckForgotPasswordCodeView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('update_language/', UpdateLanguageView.as_view()),
    path('ratings/', UserRatingListAPIView().as_view()),
    path('score/', UserScoreRatingAPIView().as_view()),
    path('leaderboard/', Leaderboard().as_view()),
    path('leaderboard_winner/', LeaderboardWinner().as_view(),)
]
urlpatterns += router.urls
