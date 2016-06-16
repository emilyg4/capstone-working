from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup

def index(request):
    return render(request, 'cruisertime/index.html')


#def index(request):
#	template = loader.get_template('polls/index.html')
#	context = {
#		'latest_question_list': latest_question_list,
#	}
#	return render(request, 'polls/index.html', context)