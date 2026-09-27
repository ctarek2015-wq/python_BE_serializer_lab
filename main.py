from fastapi import FastAPI
from controllers.posts import router as PostsRouter
from controllers.comments import router as CommentsRouter

app = FastAPI()
app.include_router(PostsRouter, prefix="/api")
app.include_router(CommentsRouter, prefix="/api")


@app.get("/")
def home():
    return {"message": "Heeeeeeeeeeeey !"}
