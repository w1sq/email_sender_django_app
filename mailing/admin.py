from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html

from .models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("subject", "created_at", "sent", "send_button")
    readonly_fields = ("sent",)

    def send_button(self, obj):
        if not obj.sent:
            url = reverse("send-mailing", args=[obj.pk])
            return format_html('<a class="button" href="{}">Отправить</a>', url)
        return "Отправлено"

    send_button.short_description = "Действия"
