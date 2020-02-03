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

    #for checkbox
    removePunc=request.GET.get('removepunc','default')
    print(removePunc)
    fullcaps=request.GET.get('fullcaps','default')
    newlinerem=request.GET.get('newlineremover','default')
    etcSpaceRemoved=request.GET.get('extraspaceremover','default')
    CountChar=request.GET.get('charactercount','default')
    #Logic for analyze text
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
    elif fullcaps=="on":
        analyzed=""
        for char in DjText:
            analyzed=analyzed+char.upper()
            params={'purpose':'Change to UpperCase','analyzed_text':analyzed}
        #Analyze the text
        return render(request,'analyze.html',params)
    elif  newlinerem=="on":
        analyzed=""
        for char in DjText:
            if char!="\n":
                analyzed=analyzed+char
        params={'purpose':'NewLines Removed','analyzed_text':analyzed}
         #Analyze the text
        return render(request,'analyze.html',params)

    elif  etcSpaceRemoved=="on":
        analyzed=""
        for index,char in enumerate(DjText):
            if DjText[index]==" "and DjText[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
            params={'purpose':'Extra Space Removed','analyzed_text':analyzed}
         #Analyze the text
        return render(request,'analyze.html',params)

    elif  CountChar=="on":
        total=0
        analyzed="Total Characters: "
        for char in DjText:
            if char==" ":
                pass
            else:
                total+=1
        total=str(total)
        analyzed+=total
        params={'purpose':'Character Counting','analyzed_text':analyzed}
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
