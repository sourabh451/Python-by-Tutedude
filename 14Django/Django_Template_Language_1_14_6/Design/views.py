from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    #return HttpResponse("<h1> Welcome </h1>")
    return render(request,'home.html', {'name':'Python'})