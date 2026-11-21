from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TodoCreate(BaseModel):
    title: str

class TodoUpdate(BaseModel):
    title: str
    completed: bool

class TodoPatch(BaseModel):
    title: str | None = None
    completed: bool | None = None

@router.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@router.post("/todos", status_code=201)
def create_todo(todo: TodoCreate):
    return {
        "message": "Todo created successfully",
        "title": todo.title,
    }

@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate):
    return {
        "id": todo_id,
        "title": todo.title,
        "completed": todo.completed,
        "message": "Todo updated",
    }

@router.patch("/todos/{todo_id}")
def patch_todo(todo_id: int, todo: TodoPatch):
    updates = todo.model_dump(exclude_unset=True)

    return {
        "id": todo_id,
        "updated_fields": updates,
        "message": "Todo partially updated",
    }

@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    return None