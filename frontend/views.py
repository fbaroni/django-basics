import json

from django.shortcuts import render
import django.http
from backend.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-title')
    context = {
        'posts': posts,
    }
    return render(request, 'list.html', context)
