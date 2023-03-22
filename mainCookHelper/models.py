from django.conf import settings
from django.db import models
from django.utils import timezone


class Recepts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=225, verbose_name="Название")
    annotation = models.TextField(verbose_name="Описание")
    ingredients = models.TextField(verbose_name="Игредиенты")
    text = models.TextField(verbose_name="Приготовление")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title