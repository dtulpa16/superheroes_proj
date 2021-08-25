from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Superhero

def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes' : all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request,hero_id):
    single_hero = Superhero.objects.get(pk = hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

