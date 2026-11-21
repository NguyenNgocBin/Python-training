from typing import Annotated

from fastapi import Depends, FastAPI

from app.core.auth import get_current_user
from app.routers.todo import router as todo_router
from app.schemas.user import User

app = FastAPI(title="Todo API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API!"}


@app.get("/me")
def read_me(user: Annotated[User, Depends(get_current_user)]) -> User:
    # FastAPI truyền User đã tra được vào tham số này.
    return user


app.include_router(todo_router)
