from __future__ import unicode_literals
from mongoengine import *
from django.db import models

# Create your models here.
class Author(Document):
    author = StringField()
    text = StringField()
        
class ObjectA(EmbeddedDocument):
    a1 = IntField()
    a2 = IntField()
    a3 = IntField()
    a4 = IntField()
    a5 = IntField()
    a6 = IntField()
    
class ObjectB(EmbeddedDocument):
    b1 = ListField()
    b2 = IntField()
    b3 = IntField()
    b4 = IntField()
    
class ObjectC(EmbeddedDocument):
    c1 = IntField()
    c2 = IntField()
    c3 = IntField()

class ObjectD(EmbeddedDocument):
    d1 = IntField()
    d2 = StringField()
    d3 = IntField()
    d4 = IntField()   
    
class System(EmbeddedDocument):
    objectA = EmbeddedDocumentField(ObjectA)
    objectB = EmbeddedDocumentField(ObjectB)
    objectC = EmbeddedDocumentField(ObjectC)
    objectD = ListField(EmbeddedDocumentField(ObjectD))
    attr1 = IntField()
    attr2 = IntField()
    attr3 = IntField()
    attr4 = IntField()
    attr5 = IntField()  
    
class Game(Document):
    system = EmbeddedDocumentField(System)
    
 
