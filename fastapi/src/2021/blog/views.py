from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from auth.helpers import get_current_user
from auth.schemas import UserCreate
from blog.models import Blog
from blog.schemas import BlogIn
from blog.schemas import BlogOut
from database import database

api = APIRouter(tags=['Blog'])


@api.post('/blog', status_code=status.HTTP_201_CREATED, response_model=BlogOut)
def post(request: BlogIn, user: UserCreate = Depends(get_current_user)):
    return Blog.insert(creator_id=1, **request.dict())


@api.get('/blog', response_model=list[BlogOut])
def list_all():
    return Blog.all()


@api.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=BlogOut)
def get(id: int, db: Session = Depends(database),
        user: UserCreate = Depends(get_current_user)):
    if result := db.query(Blog).filter(Blog.id == id).first():
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Blog does not exist')


@api.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database),
           user: UserCreate = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Blog does not exist')
    blog.delete(synchronize_session=False)
    db.commit()


@api.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def put(id: int, request: BlogOut, db: Session = Depends(database),
        user: UserCreate = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Blog does not exist')
    blog.update(request)
    db.commit()
    return request
