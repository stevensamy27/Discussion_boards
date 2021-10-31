# from typing_extensions import ParamSpecKwargs
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from .models import Board 

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'home.html', {'boards':boards})


def board_topics(reqest,board_id):
    board =get_object_or_404 (Board, pk=board_id)
    return render(reqest,'topics.html',{'board':board})


def about(reqest):
    return HttpResponse(reqest,"yes")