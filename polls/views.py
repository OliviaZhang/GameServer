from django.http import HttpResponse
from django.template import loader

def index(request):
    #return HttpResponse("sss")
    questions = [{'id':1, 'text':'t1'}]
    template = loader.get_template('polls/index.html')
    context = {
        'questions': questions
    }
    return HttpResponse(template.render(context, request))
    
def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)
def results(request, question_id):
    response = "You are looking at results of %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
