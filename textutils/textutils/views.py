#Created File
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")
def analyze(request):
    #Get text
    DjText=request.GET.get('text','default')
    print(DjText)
    removePunc=request.GET.get('removepunc','default')
    print(removePunc)
    if removePunc=="on":
        punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed= ""
        for char in DjText:
            if char not in punctuations:
                analyzed=analyzed+char
        print(analyzed)
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        #Analyze the text
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("<h1>ERROR</h1>")


'''def capfirst(request):
   return HttpResponse("Capitalize First")
def newlineremove(request):
    return HttpResponse("New Line Removed")
def spaceremover(request):
    return HttpResponse("Space Removed <a href='/'>Back</a>")
def charcount(request):
    return HttpResponse("Character Count")
'''
