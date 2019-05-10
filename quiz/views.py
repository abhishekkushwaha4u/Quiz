from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import multiple_choice
from .serializers import multiple_choiceSerializer

def home_page(request):
    return render(request,"quiz/home.html")

def about(request):
    return HttpResponse("This is about page")

# for QuizAPI
class multiple_choice_new(APIView):
    def get(self,request):
        objects = multiple_choice.objects.all()
        serializer = multiple_choiceSerializer(objects,many=True)
        return Response(serializer.data)
    def post(self,request):
        objects = multiple_choice.objects.all()
        serializer = multiple_choiceSerializer(objects,many=True)
        return Response(serializer.data)
# To add new questions
def add_question(request):
    if request.method=="GET":
        return render(request, "quiz/question.html")
    else:
        objects = multiple_choice.objects.values_list('question_number',flat=True)
        if len(objects)==0:
            q_no = 1
        else:
            q_no=list(objects)[-1]+1 
        question = request.POST.get("question")
        answer = request.POST.get("answer")
        a = request.POST.get("a")
        b = request.POST.get("b")
        c = request.POST.get("c")
        d = request.POST.get("d")
        new_question = multiple_choice(question=question, answer=answer, question_number=q_no, a=a, b=b, c=c, d=d)
        new_question.save()
        return HttpResponse("Success")

def quiz_page(request):
    question = multiple_choice.objects.all()
    context = []

    for q in question:
        context.append({"question_number":q.question_number,"question":q.question,"a":q.a,"b":q.b,"c":q.c,"d":q.d})
    print(context)
    return render(request, "quiz/quiz_page.html",{"context":context})

def answer(request):
    if request.method=="POST":
        score=0
        L=dict(request.POST)
        if 'A' not in L:
            A=[]
        else:
            A=map(int,L['A'])
        if 'B' not in L:
            B=[]
        else:
            B=map(int,L['B'])
        if 'C' not in L:
            C=[]
        else:
            C=map(int,L['C'])
        if 'D' not in L:
            D=[]
        else:
            D=map(int,L['D'])

        Q = multiple_choice.objects.all()
        M=dict(zip([i for i in range(1,Q[len(Q)-1].question_number+1)],[[] for i in range(1,Q[len(Q)-1].question_number+1)]))
        print(M)
        for i in A:
            M[i].append('A')
        for i in B:
            M[i].append('B')
        for i in C:
            M[i].append('C')
        for i in D:
            M[i].append('D')
        print(M)
        print([i.answer for i in Q ])
        for i in Q:
            if M[i.question_number]==[]:
                print("You did not attempt question number {}".format(i.question_number))
                pass
            elif len(i.answer.split(','))==len(M[i.question_number]):
                if list(i.answer.split(','))==M[i.question_number]:
                    print("You scored +4 for correct entries")
                    score+=4
                else:
                    print("You scored -1 for incorrect entries with partial or no options correct")
                    score-=1
            elif len(i.answer.split(','))>len(M[i.question_number]):
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
        return HttpResponse("Done! Your score is "+str(score))
    else:
        return HttpResponse("Access Restricted!")

        




