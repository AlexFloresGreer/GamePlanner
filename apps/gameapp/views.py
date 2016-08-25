from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from ..loginreg.models import User
from .models import GameType, Game
import bcrypt
import datetime
# from datetime import datetime

def landing(request):
    return render(request, 'gameapp/landing.html')

def join(request):
    return render(request, 'gameapp/join.html')

def start(request):
    return render(request, 'gameapp/start.html')

#Create & validations
def start_game(request):
    return redirect('/join')

def info(request):
    return render(request, 'gameapp/info.html')
