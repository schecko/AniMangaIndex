from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def detail(request, questionId):
    return HttpResponse("You're looking at question %s." % questionId)

def results(request, questionId):
    return HttpResponse("You're looking at the results of question %s." % questionId)

def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)

def index(request):
    questionList = Question.objects.order_by('-pub_date')[:5]
    
    return HttpResponse("Hello, world. You're at the polls index!!!!.")
