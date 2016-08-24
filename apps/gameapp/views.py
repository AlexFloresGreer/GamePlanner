from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from ..loginreg.models import User
import bcrypt
import datetime
# from datetime import datetime

def gamelanding(request):
    return render(request, 'gameapp/gamelanding.html')

def join(request):
    return render(request, 'gameapp/join.html')

def start(request):
    return render(request, 'gameapp/start.html')

#Create & validations
def start_game(request):
    return redirect('/dashboard')

def gameinfo(request):
    return render(request, 'gameapp/gameinfo.html')
