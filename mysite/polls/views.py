from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Works</h1>")

def details(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Voting on question {question_id}")
