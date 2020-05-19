from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request,*args, **kwargs):
    return render(request, 'index.html', {"List": [1, 3, 24, 5]})

def blog_view(request,*args, **kwargs):
    return HttpResponse('<h1>My Blog</h1>')
