from django.http import HttpResponse
from django.shortcuts import render

# Code for video: 6
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def analyze(request):
        djtext = request.POST.get('text', 'default')
        removepunc = request.POST.get('removepunc', 'off')
        fullcaps = request.POST.get('fullcaps', 'off')
        newlineremover = request.POST.get('newlineremover', 'off')
        extraspaceremover = request.POST.get('extraspaceremover', 'off')
        charcount= request.POST.get('charcount', 'off')

        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            djtext = analyzed


        if fullcaps == "on":
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
            djtext = analyzed
            # return render(request, 'analyze.html', params)

        if newlineremover == "on":
            analyzed = ""
            for char in djtext:
                if char != "\n" and char != "\r":
                    analyzed = analyzed + char
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed

        if (extraspaceremover == "on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if not (djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + char

            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            djtext = analyzed




        if (charcount == "on"):
            analyzed = ""
            i = 0
            for char in djtext:
                i = i + 1
                analyzed = i
            params = {'purpose': 'charcount', 'analyzed_text': analyzed}

        if (
                removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
            return HttpResponse("please select something")
        return render(request, 'analyze.html', params)











