from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    print(removepunc)
    print(djtext)
    # analyzed=djtext
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params={'purpose':'Change To Uppercase', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed= analyzed + char
        params={'purpose':'Removed NewLines', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1]==" "):
                analyzed= analyzed + char
        params={'purpose':'Extra Spaces Removed', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(charcount=="on"):
        analyzed=""
        i=0
        for i in range(0,len(djtext)):
            i+=1
            i=str(i)
        params={'purpose':'Characters counted', 'analyzed_text':i}
        
        # return render(request, 'analyze.html', params)
    if(removepunc !="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
    
# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount")



