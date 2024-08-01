from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #output = "".join([q.question_text for q in latest_question_list])
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist!")
    return render(request, "polls/details.html", {"question": question})

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Voting on question {question_id}")
