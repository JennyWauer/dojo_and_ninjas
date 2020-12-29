from django.shortcuts import render

from .models import *

# Create your views here.


def index(request):
    context = {
        "dojo": Dojo.objects.all(),
        "ninja": Ninja.objects.all(),
    }
    return render(request, 'index.html', context)
