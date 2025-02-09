from mongoengine import connect, Document

class BaseDAO:
    model: Document = None

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int):
        return cls.model.objects(_id = data_id)

    @classmethod
    async def find_all(cls, **filter_by):
        return cls.model.objects(**filter_by)

    @classmethod
    async def add(cls, **values):
        cls.model(**values).save()