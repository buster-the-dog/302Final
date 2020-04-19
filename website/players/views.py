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
            }
    return HttpResponse(template.render(context, request))
