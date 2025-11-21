from fastapi import APIRouter, HTTPException
from starlette import status

from app.schemas.user_schema import UserAuth
from app.services.user_service import UserService
import pymongo
from pymongo import errors

user_router = APIRouter()

@user_router.post('/adiciona', summary='adiciona usuario')
async def adiciona_usuario(data:UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='usuário ou email deste usuário já existe!'
        )
