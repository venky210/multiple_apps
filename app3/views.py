from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def dev(request):
    return render(request,'dev2.html')

def developer(request):
    return HttpResponse('<h1><marquee>Hii hacker how are you</h1></marquee>')

