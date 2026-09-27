from pydantic import BaseModel
from typing import Optional, List
from .comment import CommentSchema


class PostSchema(BaseModel):
    id: Optional[int] = True
    title: str
    content: str
    author: str
    comments: List[CommentSchema] = []

    class Config:
        orm_mode = True


# these are for req.body
class CreatePostSchema(BaseModel):
    title: str
    content: str
    author: str

    class Config:
        orm_mode = True


class UpdatePostSchema(BaseModel):
    title: str
    content: str
    author: str

    class Config:
        orm_mode = True
