from mongoengine.fields import StringField, DateTimeField, EmailField
from mongoengine import connect, Document

connect('apidb', host='localhost', port=27017)

class User(Document):
    email = EmailField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
    sign_up_datetime = DateTimeField(default=datetime.datetime.now)

ross = User(email='ross@example.com', password='Ross').save()
print(ross)