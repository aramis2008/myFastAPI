from mongoengine.fields import StringField, DateTimeField, EmailField, BooleanField
from mongoengine import Document
import datetime

class User(Document):
    name = StringField(max_length=200)
    email = EmailField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
    sign_up_datetime = DateTimeField(default=datetime.datetime.now)

    is_user = BooleanField(required=True, default=True)
    is_admin = BooleanField(required=True, default=False)
    is_super_admin = BooleanField(required=True, default=False)