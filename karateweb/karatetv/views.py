from django.shortcuts import render, redirect,  get_object_or_404
from .forms import PostForm
from django.utils import timezone
from .models import Post

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
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'karatetv/post_list_se.html', {'posts': posts})



def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'karatetv/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'karatetv/post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #post = Post.objects.get(pk=pk)
    return render(request, 'karatetv/post_detail.html', {'post': post})




