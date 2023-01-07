from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_mail(recipient, message):
    sleep(10)
    send_mail(
        "Feedback", 
        f"{message},Thank you for your feedback", 
        "secondgame@gmail.com", 
        [recipient]
        )