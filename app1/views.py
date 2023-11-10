from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def uday(request):
    return render(request,'dev1.html')

def pavan(request):
    return HttpResponse('<h1> hii pavan</h1>')