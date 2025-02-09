from app.dao.base import BaseDAO
from app.user.model import User

class StudentDAO(BaseDAO):
    model = User