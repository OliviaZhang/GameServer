from django.http import HttpResponse
from django.template import loader
import pymongo
from pymongo import MongoClient
from mongoengine import connect
import mongoengine
from django.conf import settings
from models import *

def index(request):
    conn = mongoengine.connect(settings._MONGODB_NAME, host=settings._MONGODB_DATABASE_HOST, port=settings._MONGODB_PORT)
    db = conn.olivia
    collection = db.game
    template = loader.get_template('polls/index.html')
    context = {
        'records': collection.find()
    }
    #author = Author(author = 'test@title.com',text = 'test content')
    #author.save()
    ''' save the game obj into db
    objectA = ObjectA(a1=545, a2=2, a3=4553, a4=45, a5=566, a6=6)
    objectB = ObjectB(b1=['ssfhfgh'], b2=2, b3=35, b4=4444)
    objectC = ObjectC(c1=14555, c2=26, c3=3)
    objectD = ObjectD(d1=16, d2='sfvbnvbnfgs', d3=4545453, d4=4455)
    system = System(objectA=objectA, objectB=objectB, objectC=objectC, objectD=[objectD], attr1=1, attr2=2, attr3=3, attr4=4, attr5=5)
    game = Game(system=system)
    game.save()
    '''
    
    return HttpResponse(template.render(context, request))

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
