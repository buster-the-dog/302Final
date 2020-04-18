from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *

# Create your views here.
def Index(request):
    player_list = Quarterback.objects.all()
    field_list = Quarterback._meta.get_fields()
    testfl = player_list[0].FieldList()
    template = loader.get_template('players/index.html')
    context = {
            'player_list': player_list,
            'field_list': field_list,
            }
    return HttpResponse(template.render(context, request))
