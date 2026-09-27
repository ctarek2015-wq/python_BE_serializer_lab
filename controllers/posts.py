from fastapi import APIRouter, Depends, HTTPException

# DB
from sqlalchemy.orm import Session
from database import get_db

# Models
from models.post import PostModel

# Serializers
from serializers.post import PostSchema, CreatePostSchema, UpdatePostSchema
from typing import List

router = APIRouter()


@router.get("/posts", response_model=List[PostSchema])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(PostModel).all()
    return posts


@router.get("/posts/{post_id}", response_model=PostSchema)
def get_posts(post_id: int, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    return post


@router.post("/posts", response_model=PostSchema, status_code=201)
def create_post(post: CreatePostSchema, db: Session = Depends(get_db)):
    new_post = PostModel(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.put("/posts/{post_id}", response_model=PostSchema)
def create_post(post: UpdatePostSchema, post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="post not found")
    post_data = post.dict(exclude_unset=True)
    for key, value in post_data.items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)

    return db_post


@router.delete("/posts/{post_id}", status_code=204)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="post not found")
    db.delete(db_post)
    db.commit
    return None
