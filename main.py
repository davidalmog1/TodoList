from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from db import SessionLocal, engine, DBContext
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import
import models


"""
all template response need to have the request pass to them
"""


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db():
    with DBContext() as db:
        yield db


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "home"})


@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return jsonable_encoder(db.query(models.Task).first())


app.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "login"} )
