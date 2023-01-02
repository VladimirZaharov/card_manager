import random
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone

from cards.forms import UserLoginForm, CardAddForm, CardEditForm
from cards.models import Card, CardHistory


@login_required(login_url='login')
def index(request):
    cards = Card.objects.all()
    context = {'cards': cards}
    return render(request, 'cards/index.html', context)


class LoginLoginView(LoginView):
    model = get_user_model()
    template_name = 'cards/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')


class LogoutLogoutView(LogoutView):
    next_page = 'login'


def cards_add(request):
    if request.method == "POST":
        form = CardAddForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data.get('cards_quantity')
            serial = form.cleaned_data.get('serial')
            validity = form.cleaned_data.get('validity')
            validity = timedelta(days=validity)
            expiration_date = validity + timezone.now()
            date_of_issue = timezone.now()
            cards_by_serial = Card.objects.filter(serial=serial)
            if cards_by_serial:
                last_item = cards_by_serial.latest('number')
                first_value = int(last_item.number) + 1
            else:
                first_value = 1
            last_value = first_value + quantity
            numbers = [str.rjust(str(value), 7, '0') for value in range(first_value, last_value)]
            cards = [Card(serial=serial, number=number, date_of_issue=date_of_issue, expiration_date=expiration_date,
                          status="N") for number in numbers]
            Card.objects.bulk_create(cards)
            return redirect('index')
    form = CardAddForm()
    context = {'form': form}
    return render(request, 'cards/cards_add.html', context)


def delete_card(request, serial, number):
    card = Card.objects.filter(serial=serial, number=number).first()
    card.delete()
    return redirect('index')


def card_edit(request, serial, number):
    card = Card.objects.filter(serial=serial, number=number).first()
    if request.method == "POST":
        card_stat = CardHistory.objects.create(card=card, sum=random.randint(1, 1000000))
        card_stat.save()
        form = CardEditForm(request.POST)
        if form.is_valid():
            status = form.cleaned_data.get('edit')
            card.status = status
            card.save()
    statistic = CardHistory.objects.filter(card=card)
    form = CardEditForm(initial={'edit': card.status, })
    context = {'card': card, 'form': form, 'statistics': statistic}
    return render(request, 'cards/card_edit.html', context)
