from pydantic import BaseModel
from typing import Optional, List
from .comment import CommentSchema


class PostSchema(BaseModel):
    id: Optional[int] = True
    content: str
    rating: int
    comments: List[CommentSchema] = []

    class Config:
        orm_mode = True


# these are for req.body
class CreatePostSchema(BaseModel):
    content: str
    rating: int

    class Config:
        orm_mode = True


class UpdatePostSchema(BaseModel):
    content: str
    rating: int

    class Config:
        orm_mode = True
