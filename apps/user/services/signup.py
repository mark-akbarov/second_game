# Rest-Framework
from rest_framework.response import Response
from rest_framework import status

# Models
from user.models import User
from user.services.verify import send_user_verify_code


def signup(first_name: str, last_name: str, email: str, username: str, password, birthday, smartphone_type, about):
    check_email = User.objects.filter(username__iexact=username)
    if check_email.exists() is True:
        if check_email.first().is_active is False:
            return Response({'detail': 'please_activate_your_account'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'username_already_exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = create_user(first_name, last_name, email, username, password, birthday, smartphone_type, about)
    send_user_verify_code(user)
    return Response({'detail': 'successfully registered'}, status=status.HTTP_201_CREATED)


def create_user(
        first_name: str,
        last_name: str,
        email: str,
        username: str,
        password=None,
        birthday=None,
        smartphone_type=None,
        about=None
):
    user = User.objects.create(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        birthday=birthday,
        smartphone_type=smartphone_type,
        about=about,
        is_active=False,
        is_staff=False,
        is_superuser=False,
    )
    if password:
        user.set_password(password)
        user.save()
    return user
