from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship
from .base import BaseModel


class CommentModel(BaseModel):

    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)

    # Specific columns for our Comments Table.
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    post = relationship("PostModel", back_populates="comments")
