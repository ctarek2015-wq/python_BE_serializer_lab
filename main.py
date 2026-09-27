from fastapi import FastAPI
from controllers.posts import router as PostsRouter

app = FastAPI()
app.include_router(PostsRouter, prefix="/api")


@app.get("/")
def home():
    return {"message": "Heeeeeeeeeeeey !"}
