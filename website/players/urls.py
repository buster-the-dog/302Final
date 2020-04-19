from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index),
    path('<str:playerType>/', views.PlayerView, name = "PlayerView"),
]
