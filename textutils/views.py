from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        return render(request,'index.html')

def analyze(request):
    #Get  the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremov=request.POST.get('newlineremov','off')
    extraspaceremov=request.POST.get('extraspaceremov','off')
    charcount=request.POST.get('charcount','off')
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''~`!@#$%^&*()-_{[}]|\:;'"<>,.?/'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation','analyzed_text': analyzed}
        #analyze the text
        return render(request,'analyze.html',params)
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper Case','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif newlineremov == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Removed','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif extraspaceremov == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]== " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif charcount == "on":
        analyzed = ""
        analyzed = "Total Characters in this sentence are: "+ str(len(djtext))
        params = {'purpose': 'Charcters Counted','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("Error")