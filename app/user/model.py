from mongoengine.fields import StringField, DateTimeField, EmailField
from mongoengine import Document
import datetime

class User(Document):
    name = StringField(max_length=200)
    email = EmailField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
    sign_up_datetime = DateTimeField(default=datetime.datetime.now)