from __future__ import unicode_literals
from mongoengine import *
from django.db import models

# Create your models here.
class Author(Document):
    author = StringField()
    text = StringField()
