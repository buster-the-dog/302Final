from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, Http404
from .sort import *
from .models import *

# Create your views here.
def Refresh(request, playerType):
    Update(playerType)
    return redirect("PlayerView", playerType = playerType)

def Index(request):
    return redirect("PlayerView", playerType = "QB")

def AllView(request):
    pTypes = { 
            "QB": Quarterback,
            "RB": RunningBack,
            "WR": WideReceiver,
            "TE": TightEnd,
            "K": Kicker,
            "DEF": Defense,
            }
    player_list = []
    for playerType in pTypes:
        for player in pTypes.get(playerType).objects.all():
            player_list.append(player)

    template = loader.get_template('players/index.html')
    context = {
            'player_list': player_list,
            'pTypes': pTypes,
            'use_common_list': True,
            }
    return HttpResponse(template.render(context,request))


def PlayerView(request, playerType):
    pTypes = { 
            "QB": Quarterback,
            "RB": RunningBack,
            "WR": WideReceiver,
            "TE": TightEnd,
            "K": Kicker,
            "DEF": Defense,
            }
    if playerType in pTypes:
        player_list = pTypes.get(playerType).objects.all()
    else:
        raise Http404("player type does not exist")

    template = loader.get_template('players/index.html')
    context = {
            'player_list': player_list,
            'pTypes': pTypes,
            'playerType': playerType,
            'use_common_list': False,
            }
    return HttpResponse(template.render(context, request))
