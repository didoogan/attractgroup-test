from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from celery import shared_task


@shared_task
def send_invitation_task(first_name, last_name, email):
    User = get_user_model()
    user, created = User.objects.get_or_create(email=email)
    if not created:
        return 'User {} already exist'.format(email)
    username = '{}_{}'.format(first_name, last_name)
    password = get_random_string(10)
    user.set_password(password)
    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    subject = "Congratulation!"
    message = "Hello {0}! You can log in on supersite.com. You password: {1}"\
        .format(email, password)
    send_mail(subject, message, 'admin@gmail.com', [email])
    return 'New user {} password: {}'.format(email, password)
