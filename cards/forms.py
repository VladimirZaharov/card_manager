from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class CardAddForm(forms.Form):
    cards_quantity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите количество карт'}))
    serial = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите серию карт'}))
    validity = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Введите срок действия карт (количество дней)'}))


class CardEditForm(forms.Form):
    CHOICES = [
        ('A', 'ACTIVE'),
        ('N', 'NOT ACTIVE'),
        ('E', 'EXPIRED'),
    ]

    edit = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
