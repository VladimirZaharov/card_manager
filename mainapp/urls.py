"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cards.views import index, LoginLoginView, LogoutLogoutView, cards_add, delete_card

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginLoginView.as_view(), name='login'),
    path('', index, name='index'),
    path('logout/', LogoutLogoutView.as_view(), name='logout'),
    path('cards_add', cards_add, name='cards_add'),
    path('delete_card/<str:serial><str:number>', delete_card, name='delete_card')
]
