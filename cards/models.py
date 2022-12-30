from django.db import models


def get_card_number():

class Card(models.Model):
    serial = models.CharField(max_length=8, blank=True)
    number = models.CardNumberField()



Список полей: серия карты, номер карты, дата выпуска карты, дата окончания активности
карты, дата использования, сумма, статус карты (не активирована/активирована/просрочена).