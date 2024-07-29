from django.shortcuts import render

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

def kontakt(request):
    return render(request, 'karatetv/kontakt.html', {})



