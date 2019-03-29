from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import *

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

