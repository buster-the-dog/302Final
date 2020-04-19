from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import *

# Create your views here.
def Index(request):
    out = ', '.join(t.__name__ for t in Player.__subclasses__())
    return HttpResponse(out)


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
            }
    return HttpResponse(template.render(context, request))
