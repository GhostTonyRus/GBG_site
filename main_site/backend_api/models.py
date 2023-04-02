from django.db import models

# Create your models here.
class Application(models.Model):
    # ваши данные
    full_name = models.CharField(verbose_name="ФИО", max_length=100, help_text="ФИО")
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=11, help_text="+7 999 99 99 999")
    email = models.EmailField(verbose_name="Email", max_length=50, help_text="Email")
    # услуга
    service = models.CharField(verbose_name="Услуга", max_length=10, help_text="Услуга")
    # бюджет
    budget = models.CharField(verbose_name="Бюджет", max_length=10, default=False, help_text="Бюджет")
    # о проекте
    about_project = models.TextField(verbose_name="О проекте", help_text="Опишите Задачу")

    def __str__(self):
        return f"{self.pk} - {self.full_name}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"