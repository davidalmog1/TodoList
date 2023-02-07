"""
Setup db and init session and general functions to interact with db
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker


SQLALCHEMY_DATABASE_URI = "sqlite:///.todo_app.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False}   # sqllit does not allow multiple request by default
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)

# create our DB modle
Base = declarative_base()

class DBContext():
    def __init__(self) -> None:
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, et, ev, traceback):
        self.db.close()