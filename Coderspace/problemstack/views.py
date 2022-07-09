from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): 
    return HttpResponse('Hello index')
def login(request): 
    return HttpResponse('Hello login')
def register(request): 
    return HttpResponse('Hello register')
def leaderboard(request): 
    return HttpResponse('Hello leaderboard')
def about(request): 
    return HttpResponse('Hello about')