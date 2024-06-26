from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Question, Choice
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    #context = {"latest_question_list":latest_question_list}
    #return HttpResponse(template.render(context, request))
    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    
class DetailView(generic.DetailView):

    model = Question
    template_name = "polls/detail.html"

    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #   raise Http404("Pytanie nie istnieje")
    #return render(request, "polls/detail.html", {"question": question})
    #return HttpResponse("You're looking at question %s." % question_id)

    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, "polls/detail.html", {"question": question})

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
    #question = get_object_or_404(Question, pk = question_id)
    #return render(request, 'polls:results.html', {'question':question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", 
            {
                "question":question,
                "error_message":"Nie wybrałeś odpowiedzi"

                })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        #przekeriuje na widok wyników dla pytania
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
