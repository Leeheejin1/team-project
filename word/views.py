from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    worddic = {}
    for word in words:
        if word in worddic:
            worddic[word] +=1
        else:
            worddic[word]=1
    return render(request,'result.html',{'full':text , 'total':len(words),'dic':worddic.items, 'len': len(text)})