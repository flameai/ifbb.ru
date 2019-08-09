from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.conf import settings

from .models import *

# Create your views here.


def index(request):
    slider_list = Slider.objects.order_by('order')

    return render(request, 'mainapp/index.html')


def page(request, slug):
    page_list = Page.objects.order_by('order')

    p = get_object_or_404(Page, slug=slug)

    if p.template==1:
        t='mainapp/page_main.html'
    elif p.template==2:
        t='mainapp/page_map.html'
    elif p.template==3:
        t='mainapp/page_news.html'
    elif p.template==4:
        t='mainapp/page_common.html'
    
    return render(request, t, locals())



def mainpage(request):
    page_list = Page.objects.order_by('order')
    slider_list = Slider.objects.order_by('order')
    MEDIA_URL=settings.MEDIA_URL
    p = get_object_or_404(Page, mainpage=True)
    return render(request, 'mainapp/page_main.html', locals())