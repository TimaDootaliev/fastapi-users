from sqlmodel import SQLModel, create_engine, Session
from .settings import db_url


engine = create_engine(db_url)


def get_session():
    with Session(engine) as session:
        return session


def create_table():
    SQLModel.metadata.create_all(engine)
