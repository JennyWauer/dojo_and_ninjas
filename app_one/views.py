from django.shortcuts import render, redirect

from .models import *

# Create your views here.


def index(request):
    context = {
        "dojo": Dojo.objects.all(),
        "ninja": Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        Dojo.objects.create(name=request.POST['name'],city=request.POST['city'],state=request.POST['state'],desc=request.POST['desc'])
        return redirect('/')

def add_ninja(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        Ninja.objects.create(dojo=Dojo.objects.get(name=request.POST['dojo']),first_name=request.POST['first_name'],last_name=request.POST['last_name'])
        return redirect('/')