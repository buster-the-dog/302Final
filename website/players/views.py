from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

# Create your views here.
def PlayerView(request):
    player_list = RunningBack.objects.all()
    template = loader.get_template('players/index.html')
    context = {
            'player_list': player_list,
            }
    return HttpResponse(template.render(context, request))
