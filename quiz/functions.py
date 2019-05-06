import random
from .models import multiple_choice
from django.http import HttpResponse
from django.shortcuts import render

def random_questions(request):
    if request.method=="GET":
        return render(request,"temp/temporary.html")
    else:    
        n = int(request.POST.get("no-of-questions"))
        p = len(multiple_choice.objects.all())
        if n>p:
            return HttpResponse('<html><head><body>Do not have enough questions in database! Enter lesser no of questions!<a href="/quiz/random/">Click here</a></body></head></html>')
        L=random.sample(range(1,p+1),n)
        return(customized_questions(request,L))
            
def customized_questions(request,L):
    context = []
    n=1
    for i in L:
        q = multiple_choice.objects.get(id=i)
        context.append({"id":q.id,"question_number":n,"question":q.question,"a":q.a,"b":q.b,"c":q.c,"d":q.d})
        n+=1
    print(context)
    return render(request, "temp/quiz_page.html",{"context":context})

def customized_response(request):
    print(dict(request.POST))
    return HttpResponse(dict(request.POST))
    





