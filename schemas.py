"""
Pidentic modele | for collection data converting to json and using it in out operation
"""

from pydantic import BaseModel
from typing import List, Optional


class TaskBase(BaseModel):
    text: str


class Task(TaskBase):
    id: str
    user_id: str

    class config:
        orm_mode = True 


class CreateTask(TaskBase):
    pass


class UserBase(BaseModel):
    username: str
    email: str
    hashed_password: str


class User(UserBase):
    id: str
    tasks: List[Task] = []

    class config:
        orm_mode = True


class UserCreate(UserBase):
    pass