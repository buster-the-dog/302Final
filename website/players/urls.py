from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllView, name = 'AllView'),
    path('<str:playerType>/', views.PlayerView, name = "PlayerView"),
    path('<str:playerType>/refresh', views.Refresh, name = "Refresh"),
]
