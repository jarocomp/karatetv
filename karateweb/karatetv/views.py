from django.shortcuts import render
from .forms import PostForm

def domov(request):
    return render(request, 'karatetv/domov.html', {})

def onas(request):
    return render(request, 'karatetv/onas.html', {})

def treneriaasistenti(request):
    return render(request, 'karatetv/treneriaasistenti.html', {})

def treningy(request):
    return render(request, 'karatetv/treningy.html', {})

def poriadok(request):
    return render(request, 'karatetv/poriadok.html', {})

def prihlaska(request):
    return render(request, 'karatetv/prihlaska.html', {})

def kontakt(request):
    return render(request, 'karatetv/kontakt.html', {})

def trebisov(request):
    return render(request, 'karatetv/trebisov.html', {})

def secovce(request):
    return render(request, 'karatetv/secovce.html', {})

def admin(request):
    return render(request, 'admin/base_site.html', {})
