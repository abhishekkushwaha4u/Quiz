import random
from collections import defaultdict
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
    #print(context)
    return render(request, "temp/quiz_page.html",{"context":context})

def customized_response(request):
    print(dict(request.POST))
    L = dict(request.POST)
    if 'A' in L:
        A = list(map(int,L['A']))
    else:
        A = []
    if 'B' in L:
        B = list(map(int,L['B']))
    else:
        B = []
    if 'C' in L:
        C = list(map(int,L['C']))
    else:
        C = []
    if 'D' in L:
        D = list(map(int,L['D']))
    else:
        D = []

    R = []
    R.extend(A)
    R.extend(B)
    R.extend(C)
    R.extend(D)
    R = list(set(R))

    print(R)
    print("A:",A)
    print("B:",B)
    print("C:",C)
    print("D:",D)
    M=defaultdict(list)
    Q={}
    for i in R:
        correct = multiple_choice.objects.get(id=int(i))
        Q[i] = (correct.answer).split(',')
    for i in A:
        M[i].append('A')
    for i in B:
        M[i].append('B')
    for i in C:
        M[i].append('C')
    for i in D:
        M[i].append('D')
    # print(M)
    # print(Q)
    score=0
    count = 1
    for i in Q:
        if M[i]==[]:
            print("You did not attempt question number {}".format(count))
        elif len(Q[i])==len(M[i]):
            if Q[i]==M[i]:
                print("You scored +4 for correct entries")
                score+=4
            else:
                print("You scored -1 for incorrect entries with partial or no options correct")
                score-=1
        elif len(Q[i])>len(M[i]):
            for i1 in M[i.question_number]:
                if i1 not in i.answer.split(','):
                    score-=1
                    print("You entered an incorrect entry out of the total options entered!")
                    break
                else:
                    pass
                print("You got partial marking of {} options out of {} options in this question".format(len(M[i.question_number]),len(i.answer.split(','))))
                score+=len(M[i.question_number])
        else:
            print("You got negative marking!")
            score-=1
        count+=1
    return HttpResponse("Done! Your score is "+str(score))

    






