from django.db import models

# Create your models here.
class Application(models.Model):
    # ваши данные
    full_name = models.CharField(verbose_name="ФИО", max_length=100, help_text="ФИО")
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=11, help_text="+7 999 99 99 999")
    email = models.EmailField(verbose_name="Email", max_length=50, help_text="Email")
    # Выберите услугу
    landing_page = models.BooleanField(verbose_name="Лендинг", default=False, help_text="Лендинг")
    business_card_website = models.BooleanField(verbose_name="Сайт-визитка", default=False, help_text="Сайт-визитка")
    corporate_website = models.BooleanField(verbose_name="Корпоративный сайт", default=False, help_text="Корпоративный сайт")
    whim = models.BooleanField(verbose_name="Каприз", default=False, help_text="Каприз")
    # бюджет
    less_than_five_hundred_thousand = models.BooleanField(verbose_name="Менее 500 Т/Р", default=False, help_text="Менее 500 Т")
    less_than_million = models.BooleanField(verbose_name="Менее Мил", default=False, help_text="Менее Мил")
    more_than_million = models.BooleanField(verbose_name="Более Мил", default=False, help_text="Более Мил")
    arbitrary_option = models.BooleanField(verbose_name="Не знаю", default=False, help_text="Не знаю")
    # о проекте
    about_project = models.TextField(verbose_name="О проекте", help_text="Опишите Задачу")

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"