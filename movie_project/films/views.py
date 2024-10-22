from django.shortcuts import render, redirect
from .models import Films
from .forms import FilmsForm

def index(request):
    films = Films.objects.all()
    return render(request, 'films/films.html', {'films': films})

def add_movie(request):
    error = ''
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'

    form = FilmsForm()
    return render(request, 'films/add_movie.html',{'form': form, 'error': error})
# Create your views here.
