from django.shortcuts import render, get_object_or_404, reverse
from django.http import *
from .models import Question, Choice
from django.template import loader


def detail(request, questionId):
    try:
        question = Question.objects.get(pk=questionId)
    except:
        raise Http404("question does not exist")
    return render(request, 'polls/detail.html', { 'question': question })

def results(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'polls/results.html', { 'question': question })

def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'errorMessage': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def index(request):
    questionList = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'questionList': questionList,
    }
    rendered = template.render(context, request)
    return HttpResponse(rendered)
