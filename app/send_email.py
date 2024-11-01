from django.core.mail import send_mail

def send_update_email(user_email, subject, message):
    send_mail(
        subject,
        message,
        'no-reply@yourplatform.com',
        [user_email],
        fail_silently=False,
    )
