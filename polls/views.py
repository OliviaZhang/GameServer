from django.http import HttpResponse
from django.template import loader
import pymongo
from pymongo import MongoClient
from mongoengine import connect
import mongoengine
from django.conf import settings

def index(request):
    conn = mongoengine.connect(settings._MONGODB_NAME, host=settings._MONGODB_DATABASE_HOST, port=settings._MONGODB_PORT)
    db = conn.olivia
    collection = db.game
    template = loader.get_template('polls/index.html')
    context = {
        'records': collection.find()
    }
    return HttpResponse(template.render(context, request))
    #for doc in  collection.find():
    #    return HttpResponse( doc['_id'])

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)
def results(request, question_id):
    response = "You are looking at results of %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
def db(request):
    '''
    conn = MongoClient("ds035965.mongolab.com", 35965)
    db = conn.olivia
    db.authenticate('olivia','gl9j8724')
    game = db.game.find()
    '''
