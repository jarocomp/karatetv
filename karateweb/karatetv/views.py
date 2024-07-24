from django.shortcuts import render

def home(request):
    return render(request, 'karatetv/home.html', {})

def onas(request):
    return render(request, 'karatetv/onas.html', {})

