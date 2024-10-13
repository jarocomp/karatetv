from django.shortcuts import render, redirect,  get_object_or_404
from .forms import PostFormSE, PostFormTV
from django.utils import timezone
from .models import PostSE, PostTV

def domov(request):
    return render(request, 'karatetv/domov.html', {})

def onas(request):
    return render(request, 'karatetv/onas.html', {})

def treneriaasistenti(request):
    return render(request, 'karatetv/treneriaasistenti.html', {})

def treningy(request):
    return render(request, 'karatetv/treningy.html', {})

def dokumenty(request):
    return render(request, 'karatetv/dokumenty.html', {})

def kontakt(request):
    return render(request, 'karatetv/kontakt.html', {})

def trebisov(request):
    return render(request, 'karatetv/trebisov.html', {})

def secovce(request):
    return render(request, 'karatetv/post_list_se.html', {})

def admin(request):
    return render(request, 'admin/base_site.html', {})

def post_list_se(request):
    post = PostSE.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'karatetv/post_list_se.html', {'posts': post})

def post_list_tv(request):
    post = PostTV.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'karatetv/post_list_tv.html', {'posts': post})



def post_new_se(request):
    if request.method == "POST":
        form = PostFormSE(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_se', pk=post.pk)
    else:
        form = PostFormSE()
    return render(request, 'karatetv/post_edit_se.html', {'form': form})

def post_new_tv(request):
    if request.method == "POST":
        form = PostFormTV(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_tv', pk=post.pk)
    else:
        form = PostFormTV()
    return render(request, 'karatetv/post_edit_tv.html', {'form': form})

def post_edit_se(request, pk):
    post = get_object_or_404(PostSE, pk=pk)
    if request.method == "POST":
        form = PostFormSE(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_se', pk=post.pk)
    else:
        form = PostFormSE(instance=post)
    return render(request, 'karatetv/post_edit_se.html', {'form': form})

def post_edit_tv(request, pk):
    post = get_object_or_404(PostTV, pk=pk)
    if request.method == "POST":
        form = PostFormTV(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_tv', pk=post.pk)
    else:
        form = PostFormTV(instance=post)
    return render(request, 'karatetv/post_edit_tv.html', {'form': form})


def post_detail_se(request, pk):
    post = get_object_or_404(PostSE, pk=pk)
    #post = Post.objects.get(pk=pk)
    return render(request, 'karatetv/post_detail_se.html', {'post': post})

def post_detail_tv(request, pk):
    post = get_object_or_404(PostTV, pk=pk)
    #post = Post.objects.get(pk=pk)
    return render(request, 'karatetv/post_detail_tv.html', {'post': post})




