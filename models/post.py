from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import relationship
from .comment import CommentModel
from .base import BaseModel


class PostModel(BaseModel):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns for our Tea Table.
    title = Column(String)
    content = Column(String)
    author = Column(String)
    comments = relationship("CommentModel", back_populates="post")
