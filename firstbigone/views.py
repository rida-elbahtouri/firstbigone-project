from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')

def count(request):
    fullwords=request.GET['fulltext']
    wordslist=fullwords.split()
    worddic={}
    for word in wordslist:
        if word in worddic:
            worddic[word] +=1
        else:
            worddic[word] =1
    order=sorted(worddic.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fullwords,'count':len(wordslist),'worddic':order})
def about(request):
    return render(request,'about.html')
