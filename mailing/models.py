from django.db import models


class Mailing(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема письма")
    message = models.TextField(verbose_name="Текст письма")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    sent = models.BooleanField(default=False, verbose_name="Отправлено")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return self.subject
