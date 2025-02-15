from mongoengine import connect, Document

class BaseDAO:
    model: Document = None

    @classmethod
    def find_one_or_none_by_id(cls, data_id: int):
        return cls.model.objects(_id = data_id)

    @classmethod
    def find_all(cls, **filter_by):
        return cls.model.objects(**filter_by)

    @classmethod
    def add(cls, **values):
        cls.model(**values).save()