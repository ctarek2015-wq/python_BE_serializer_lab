from sqlalchemy import Column, Integer, String, Boolean

from sqlalchemy.orm import relationship
from .comment import CommentModel
from .base import BaseModel


class PostModel(BaseModel):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns for our Tea Table.
    content = Column(String)
    rating = Column(Integer)
    comments = relationship("CommentModel", back_populates="post")
