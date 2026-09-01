from pydantic import BaseModel, EmailStr
from datetime import datetime


# Base schema
class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int


# Schema for creating a user
class UserCreate(UserBase):
    pass


# Schema for updating a user
class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None


# Schema for returning user data
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int


    class Config:
        from_attributes = True