from fastapi import APIRouter, HTTPException, status
from app.user.dao import UserDAO
from app.user.auth import get_password_hash
from app.user.api_input_schemas import SUserRegister

router = APIRouter(prefix='/user', tags=['Все пользователи'])

@router.get("/{email}", summary="Получить пользователя по почте")
def get_student_by_email(email: str):
    rez = UserDAO.find_one_or_none_by_email(email=email)
    if rez is None:
        return {'message': f'Пользователь с email "{email}" не найден!'}
    return rez

@router.get("/by_filter", summary="Получить одного пользователя по фильтру")
def get_student_by_filter(request_body):
    rez = UserDAO.find_all(**request_body.to_dict())
    if rez is None:
        return {'message': f'Пользователь с указанными вами параметрами не найден!'}
    return rez

@router.post("/register/")
def register_user(user_data: SUserRegister):
    user = UserDAO.find_one_or_none_by_email(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    UserDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}