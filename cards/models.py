from django.db import models
from cards.fields import CardNumberField


class Card(models.Model):
    ACTIVE = 'A'
    NOT_ACTIVE = 'N'
    EXPIRED = 'E'

    STATUS_CHOICES = (
        (ACTIVE, 'A'),
        (NOT_ACTIVE, 'N'),
        (EXPIRED, 'E')
    )

    serial = models.CharField(max_length=8, blank=True)
    number = CardNumberField(null=True, max_length=8, editable=False)
    date_of_issue = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    sum = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True)


class CardHistory(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    sum = models.DecimalField(default=0, max_digits=9, decimal_places=2)