from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def virat(request):
    return render(request,'rcb.html')

def msd(request):
    return HttpResponse('<h1>IPL 360</h1>')
