# from typing_extensions import ParamSpecKwargs
from django.core.checks import messages
from .forms import NewTopicForm
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, response
from .models import Board, Topic
from django.contrib.auth.models import  User
from.models import Topic,Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'home.html', {'boards':boards})


def board_topics(request,board_id):
    board =get_object_or_404 (Board, pk=board_id)
    return render(request,'topics.html',{'board':board})


@login_required
def new_topic(request,board_id):
    board =get_object_or_404 (Board, pk=board_id)
    # form = NewTopicForm()
    # user = User.objects.first()
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                created_by = request.user,
                topic = topic

            )
            return redirect('board_topics',board_id=board.pk)

    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board':board, 'form':form})



def topic_posts(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
    return render(request,'topic_posts.html',{'topic':topic})


def about(request):

    return HttpResponse(request,"yes")
