from django.http import *
from .models import Question
from django.shortcuts import *

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

def results(request, question_id):
    resp = "You're looking at the results for question %s."
    return HttpResponse(resp % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
