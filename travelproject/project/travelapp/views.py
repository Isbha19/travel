from django.http import HttpResponse
from django.shortcuts import render
from .models import Team,Travel

# Create your views here.

def demo(request):
    x=Team.objects.all()
    a = Travel.objects.all()
    return render(request,'index.html',{"dic":x,"res":a})

