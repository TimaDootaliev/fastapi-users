from fastapi import APIRouter, Depends
from sqlmodel import Session

from .queries import register_user, get_users
from .models import User
from app.database import get_session


router = APIRouter(
    prefix='/auth'
)


@router.post('/register')
def register(data: User, session: Session = Depends(get_session)):
    user = register_user(data, session)
    return {'message': f'{user.username} registered successfully!'}


@router.get('/users')
def get_all_users(session: Session = Depends(get_session)):
    query = get_users(session)
    return query
