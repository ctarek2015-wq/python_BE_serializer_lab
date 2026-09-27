from fastapi import APIRouter, Depends, HTTPException

# DB
from sqlalchemy.orm import Session
from database import get_db

# Models
from models.post import PostModel
from models.comment import CommentModel

# Serializers
from serializers.post import PostSchema, CreatePostSchema, UpdatePostSchema
from serializers.comment import CommentSchema, CreateCommentSchema, UpdateCommentSchema
from typing import List

router = APIRouter()


@router.get("/posts/{post_id}/comments", response_model=List[CommentSchema])
def get_comments(post_id: int, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    return post.comments


@router.get("/comments/{comment_id}", response_model=CommentSchema)
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="comment not found")
    return comment


@router.post("/posts/{post_id}/comments", response_model=CommentSchema, status_code=201)
def create_comment(
    post_id: int, comment: CreateCommentSchema, db: Session = Depends(get_db)
):
    post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    new_comment = CommentModel(**comment.dict(), post_id=post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@router.put("/comments/{comment_id}", response_model=CommentSchema)
def update_comment(
    comment_id: int, comment: UpdateCommentSchema, db: Session = Depends(get_db)
):
    db_comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="comment not found")
    comment_data = comment.dict(exclude_unset=True)
    for key, value in comment_data.items():
        setattr(db_comment, key, value)

    db.commit()
    db.refresh(db_comment)

    return db_comment


@router.delete("/comments/{comment_id}", status_code=204)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = db.query(CommentModel).filter(CommentModel.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=404, detail="comment not found")
    db.delete(db_comment)
    db.commit()
    return None
