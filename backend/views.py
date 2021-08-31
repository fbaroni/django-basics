import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm
from backend.models import Post

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/frontend/')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)