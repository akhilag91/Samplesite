from django.conf.urls import url
from django.contrib import admin

from ourspace import views

urlpatterns = [
    url(r'home/', views.home, name='home'),
]