from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.

def signup(reqest):

    form = UserCreationForm()
    return render(reqest,'signup.html', {'form':form})