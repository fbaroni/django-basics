from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import PostForm
from django.core.serializers import serialize
from backend.models import Post
from backend.serializers import PostSerializer

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

def get_json(request):
    post = Post.objects.all()
    return HttpResponse(serialize('json', post, cls=PostSerializer), content_type="application/json")

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return HttpResponse(serialize('json', [post], cls=PostSerializer), content_type="application/json")