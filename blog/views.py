from django.http.response import HttpResponse
from django.shortcuts import render ,HttpResponse
from django.utils.text import slugify
from .models import post

# Create your views here.

def blog(request):
    allPost=post.objects.all()
    data={
        "allPost":allPost,
    }
    return render(request,'blog/bloghome.html',data)
def blogpost(request,slug):
    Post=post.objects.filter(post_slug=slug).first()
    data={
        'post':Post,
    }
    return render(request,'blog/blogpost.html',data)
