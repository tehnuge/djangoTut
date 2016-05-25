import json
from django.http import HttpResponse, Http404
from .models import Question
from django.template import RequestContext

from django.shortcuts import render, get_object_or_404, render_to_response

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
		'title': json.dumps({'title': 'secretsss!'})
	}
	return render_to_response('polls/index.html', RequestContext(request, context))

def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("you're voting on question %s" % question_id)

