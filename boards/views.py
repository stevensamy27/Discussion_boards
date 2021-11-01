# from typing_extensions import ParamSpecKwargs
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, response
from .models import Board, Topic
from django.contrib.auth.models import  User
from.models import Topic,Post

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'home.html', {'boards':boards})


def board_topics(request,board_id):
    board =get_object_or_404 (Board, pk=board_id)
    return render(request,'topics.html',{'board':board})

def new_topic(request,board_id):
    board =get_object_or_404 (Board, pk=board_id)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()

        # topic = Topic.objects.create(
        #     subject = subject,
        #     board = board_id,
        #     created_by = user,
        # )

        # post = Post.objects.create(
        #     message = message,
        #     topic = topic,
        #     created_by = user,
            
        # ) 
        return redirect('board_topics', board_id= board.pk)

    return render(request, 'new_topic.html', {'board':board})

def about(request):
    return HttpResponse(request,"yes")