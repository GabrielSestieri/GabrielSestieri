from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("hello, world")
# Create your views here.
