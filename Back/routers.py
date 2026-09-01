from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schema import UserResponse, UserCreate, UserUpdate
import crud


router = APIRouter(
    prefix="/users"
)


# CREATE
@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db, user)


# READ ALL
@router.get("/", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return crud.get_users(db)


# UPDATE
@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_user(db, user_id, user)


# DELETE
@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_user(db, user_id)