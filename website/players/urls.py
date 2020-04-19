from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlayerView, name='index'),
]
