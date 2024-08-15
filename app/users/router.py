from fastapi import APIRouter, HTTPException, status, Response, Depends
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependecies import get_current_user, get_current_admin_user
from app.users.models import User
from app.users.schemas import SUserRegister, SUserAuth, SUserSetPrivilege

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/")
async def register_user(user_data: SUserRegister) -> dict:
    user = await UsersDAO.find_one_or_none(email=user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.dict()
    user_dict['password'] = get_password_hash(user_data.password)
    await UsersDAO.add(**user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}


@router.post("/login/")
async def auth_user(response: Response, user_data: SUserAuth):
    check = await authenticate_user(email=user_data.email, password=user_data.password)
    if not check:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Wrong email or password')
    access_token = create_access_token({'sub': str(check.id)})
    response.set_cookie(key='users_access_token', value=access_token, httponly=True)
    return {'ok': True, 'access_token': access_token, 'refresh_token': None, 'message': 'Авторизация успешна!'}


@router.get("/me")
async def get_me(user_data: User = Depends(get_current_user)):
    return user_data


@router.get("/all_users/")
async def get_all_users(user_data: User = Depends(get_current_admin_user)):
    return await UsersDAO.find_all()


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}


@router.post("/set_privilege/")
async def set_user_privilege(set_user_data: SUserSetPrivilege, user_data: User = Depends(get_current_admin_user)):
    check = await UsersDAO.update(filter_by={"email": set_user_data.email},
                                  privilege_id=set_user_data.privilege_id)
    if check:
        return {"message": f"Роль успешно обновлена на {set_user_data.privilege_id}"}
    else:
        return {"message": "Что-то пошло не так"}
