#Created File
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Home")
def removepunc(request):
    return HttpResponse("remove punc")
def capfirst(request):
    return HttpResponse("Capitalize First")
def newlineremove(request):
    return HttpResponse("New Line Removed")
def spaceremover(request):
    return HttpResponse("Space Removed <a href='/'>Back</a>")
def charcount(request):
    return HttpResponse("Character Count")

