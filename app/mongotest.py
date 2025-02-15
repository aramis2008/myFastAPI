import sys
import os

current_dir = os.path.dirname(__file__)
proj_path = os.path.dirname(current_dir)
sys.path.insert(0, proj_path)

from mongoengine import connect
from app.user.dao import UserDAO

connect('apidb', host='localhost', port=27017)


print(UserDAO.find_one_or_none_by_name('zoro')[0].name)

