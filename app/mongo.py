from mongoengine import connect
from app.user.dao import BaseDAO

connect('apidb', host='localhost', port=27017)

print(BaseDAO.find_all())
