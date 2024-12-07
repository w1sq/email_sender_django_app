import logging

from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.mail import send_mass_mail, get_connection

from .models import Mailing
from users.models import User

logger = logging.getLogger(__name__)


class SendMailingView(APIView):
    def get(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        if mailing.sent:
            return Response(
                {"error": "Это письмо уже было отправлено"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        users = User.objects.all()

        if not users.exists():
            return Response(
                {"error": "Нет получателей для рассылки"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        emails = [
            (
                mailing.subject,
                mailing.message,
                settings.EMAIL_HOST_USER,
                [user.email],
            )
            for user in users
        ]

        try:
            connection = get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_HOST_USER,
                password=settings.EMAIL_HOST_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS,
            )

            send_mass_mail(emails, fail_silently=False, connection=connection)

            mailing.sent = True
            mailing.save()
            logger.info("Mailing %s sent successfully", mailing.id)
            return Response(
                {
                    "message": "Рассылка успешно отправлена",
                    "recipients": list(users.values_list("email", flat=True)),
                }
            )

        except Exception as e:
            logger.error("Failed to send emails: %s", str(e), exc_info=True)
            return Response(
                {
                    "error": str(e),
                    "details": "Проверьте настройки SMTP и учетные данные",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
