from app.dao.base import BaseDAO
from app.user.model import User

class UserDAO(BaseDAO):
    model = User

    @classmethod
    def find_one_or_none_by_name(cls, name: str):
        return cls.model.objects(name = name)