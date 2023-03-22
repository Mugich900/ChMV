from django.shortcuts import render, get_object_or_404, redirect
from .models import Recepts
from django.utils import timezone
from .forms import ReceptForm
from django.db.models import Q

# Create your views here.

def index(request):
    posts = Recepts.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'mainCookHelper/index.html', {'posts': posts})

def login(request):
    return render(request, 'registration/login.html', {})

def logout(request):
    return render(request, 'registration/logout.html', {})

def recept_detail(request, pk):
    post = get_object_or_404(Recepts, pk=pk)
    return render(request, 'mainCookHelper/recept_detail.html', {'post': post})

def recept_new(request):
    title = "Создать рецепт"
    if request.method == 'POST':
        form = ReceptForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('recept_detail', pk=post.pk)
    else:
        form = ReceptForm()
    return render(request, 'mainCookHelper/recept_new.html', {'form': form, 'title':title})

def recept_edit(request, pk):
    title = "Редактировать рецепт"
    post = get_object_or_404(Recepts, pk=pk)
    if request.method == "POST":
        form = ReceptForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('recept_detail', pk=post.pk)
    else:
        form = ReceptForm(instance=post)
    return render(request, 'mainCookHelper/recept_new.html', {'form': form, 'title':title})

def recept_delete(request, pk):
    post = get_object_or_404(Recepts, id=pk)
    post.delete()
    return redirect(index)
