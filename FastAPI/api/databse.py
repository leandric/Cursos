from sqlmodel import create_engine, Session, SQLModel, select
from pathlib import Path

from api.models import Livro

DATABASE_PATH = Path("databse.db")
DATABSE_URL = f"sqlite:///{DATABASE_PATH}"
CONNECT_ARGS = {"check_same_thread":False}

engine = create_engine(DATABSE_URL, connect_args=CONNECT_ARGS)

def criar_db_tabelas():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session