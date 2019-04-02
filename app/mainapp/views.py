from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

from .models import *

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def page(request, slug):
    p = get_object_or_404(Page, slug=slug)
    return render(request, 'mainapp/page_map.html', locals())