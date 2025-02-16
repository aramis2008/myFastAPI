from fastapi import APIRouter, Depends
from app.user.dao import UserDAO

router = APIRouter(prefix='/user', tags=['Все пользователи'])

@router.get("/{email}", summary="Получить пользователя по почте")
async def get_student_by_email(email: str):
    rez = await UserDAO.find_one_or_none_by_email(email=email)
    if rez is None:
        return {'message': f'Пользователь с email "{email}" не найден!'}
    return rez

@router.get("/by_filter", summary="Получить одного пользователя по фильтру")
async def get_student_by_filter(request_body):
    rez = await UserDAO.find_all(**request_body.to_dict())
    if rez is None:
        return {'message': f'Пользователь с указанными вами параметрами не найден!'}
    return rez