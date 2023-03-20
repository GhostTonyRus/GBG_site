from django.db import models

# Create your models here.
class Application(models.Model):
    # ваши данные
    full_name = models.CharField(verbose_name="ФИО", max_length=100, help_text="ФИО")
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=11, help_text="+7 999 99 99 999")
    email = models.EmailField(verbose_name="Email", max_length=50, help_text="Email")
    # Выберите услугу
    landing_page = models.CharField(verbose_name="Лендинг", max_length=10, help_text="Лендинг")
    business_card_website = models.CharField(verbose_name="Сайт-визитка", max_length=10, help_text="Сайт-визитка")
    corporate_website = models.CharField(verbose_name="Корпоративный сайт", max_length=10, help_text="Корпоративный сайт")
    whim = models.CharField(verbose_name="Каприз", max_length=10, help_text="Каприз")
    # бюджет
    less_than_five_hundred_thousand = models.CharField(verbose_name="Менее 500 Т/Р", max_length=10, help_text="Менее 500 Т")
    less_than_million = models.CharField(verbose_name="Менее Мил", max_length=10, help_text="Менее Мил")
    more_than_million = models.CharField(verbose_name="Более Мил", max_length=10, help_text="Более Мил")
    arbitrary_option = models.CharField(verbose_name="Не знаю", max_length=10, help_text="Не знаю")
    # о проекте
    about_project = models.TextField(verbose_name="О проекте", help_text="Опишите Задачу")

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"