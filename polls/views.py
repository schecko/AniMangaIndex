from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader


def detail(request, questionId):
    try:
        question = Question.objects.get(pk=questionId)
    except:
        raise Http404("question does not exist")
    return render(request, 'polls/detail.html', { 'question': question })

def results(request, questionId):
    return HttpResponse("You're looking at the results of question %s." % questionId)

def vote(request, questionId):
    return HttpResponse("You're voting on question %s." % questionId)

def index(request):
    questionList = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'questionList': questionList,
    }
    rendered = template.render(context, request)
    return HttpResponse(rendered)
