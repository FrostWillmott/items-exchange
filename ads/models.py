from django.contrib.auth.models import User
from django.db import models


class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image_url = models.URLField(max_length=500, verbose_name="Ссылка на изображение")
    category = models.CharField(max_length=100, verbose_name="Категория")
    condition = models.CharField(max_length=50, verbose_name="Состояние")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title


class ExchangeProposal(models.Model):
    STATUS_CHOICES = [
        ("ожидает", "Ожидает"),
        ("принята", "Принята"),
        ("отклонена", "Отклонена"),
    ]

    ad_sender = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="sent_proposals", verbose_name="Отправитель объявления")
    ad_receiver = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="received_proposals", verbose_name="Получатель объявления")
    comment = models.TextField(verbose_name="Комментарий", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ожидает", verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"От {self.ad_sender} к {self.ad_receiver} - {self.status}"
