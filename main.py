from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
import uuid

app = FastAPI()


db = {
    "users": [],
    "tasks": [],
    "notes": [],
    "books": [],
    "posts": []
}

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


class Task(BaseModel):
    id: int
    title: str
    description: str


class Note(BaseModel):
    id: int
    content: str


class Book(BaseModel):
    id: int
    title: str
    author: str


class Post(BaseModel):
    id: int
    title: str
    body: str


# Users service
@app.get("/users/", tags=["Users"])
def get_users():
    return db["users"]


@app.post("/users/", tags=["Users"])
def create_user(user: User):
    db["users"].append(user.dict())
    return db["users"]


@app.put("/users/{user_id}", tags=["Users"])
def update_user(user_id: int, user: User):

    for u_id, u in enumerate(db["users"]):
        if u["id"] == user_id:
            # Kullanıcıyı güncelle
            db["users"][u_id] = user.dict()
            return user
    # Kullanıcı bulunamazsa HTTP 404 hatası döndür
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id: int):
    for u_id, user in enumerate(db["users"]):
        if user["id"] == user_id:
            del db["users"][u_id]
            return {"message": "User deleted successfully"}

    raise HTTPException(status_code=404, detail="User not found")


# Tasks service
@app.get("/tasks/", tags=["Tasks"])
def get_tasks():
    return db["tasks"]


@app.post("/tasks/", tags=["Tasks"])
def create_task(task: Task):
    db["tasks"].append(task.dict())
    return task


@app.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task: Task):
    for t_id, t in enumerate(db["tasks"]):
        if t["id"] == task_id:
            db["tasks"][t_id] = task.dict()
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    for t_id, task in enumerate(db["tasks"]):
        if task["id"] == task_id:
            del db["tasks"][t_id]
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")


# Notes service
@app.get("/notes/", tags=["Notes"])
def get_notes():
    return db["notes"]


@app.post("/notes/", tags=["Notes"])
def create_note(note: Note):
    db["notes"].append(note.dict())
    return note


@app.put("/notes/{note_id}", tags=["Notes"])
def update_note(note_id: int, note: Note):
    for n_id, n in enumerate(db["notes"]):
        if n["id"] == note_id:
            db["notes"][n_id] = note.dict()
            return note

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/notes/{note_id}", tags=["Notes"])
def delete_note(note_id: int):
    for n_id, note in enumerate(db["notes"]):
        if note["id"] == note_id:
            del db["notes"][n_id]
            return {"message": "Note deleted successfully"}

    raise HTTPException(status_code=404, detail="Note not found")


# Books service
@app.get("/books/", tags=["Books"])
def get_books():
    return db["books"]


@app.post("/books/", tags=["Books"])
def create_book(book: Book):
    db["books"].append(book.dict())
    return book


@app.put("/books/{book_id}", tags=["Books"])
def update_book(book_id: int, book: Book):
    for b_id, b in enumerate(db["books"]):
        if b["id"] == book_id:
            db["books"][b_id] = book.dict()
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", tags=["Books"])
def delete_book(book_id: int):
    for b_id, book in enumerate(db["books"]):
        if book["id"] == book_id:
            del db["books"][b_id]
            return {"message": "Book deleted successfully"}

    raise HTTPException(status_code=404, detail="Book not found")


# Posts service
@app.get("/posts/", tags=["Posts"])
def get_posts():
    return db["posts"]


@app.post("/posts/", tags=["Posts"])
def create_post(post: Post):
    db["posts"].append(post.dict())
    return post


@app.put("/posts/{post_id}", tags=["Posts"])
def update_post(post_id: int, post: Post):
    for b_id, p in enumerate(db["books"]):
        if p["id"] == post_id:
            db["posts"][b_id] = post.dict()
            return post

    raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/posts/{post_id}", tags=["Posts"])
def delete_post(post_id: int):
    for p_id, post in enumerate(db["posts"]):
        if post["id"] == post_id:
            del db["posts"][p_id]
            return {"message": "Post deleted successfully"}

    raise HTTPException(status_code=404, detail="Post not found")


# Authentication service
@app.post("/login/", tags=["Authentication"])
async def login(user_email: str, user_password: str):
    for u in db["users"]:
        if u['email'] == user_email and u['password'] == user_password:
            token = str(uuid.uuid4())
            # Oturum belirtecini kullanıcı nesnesine ekleyelim
            u['token'] = token
            return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid email or password")


@app.post("/logout/", tags=["Authentication"])
async def logout(user_token: str):
    for u in db["users"]:
        if u["token"] == user_token:
            u["token"] = None
            return {"message": "Logged out successfully"}
    raise HTTPException(status_code=404, detail="User not found")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
