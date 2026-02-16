from sqlmodel import create_engine, Session, SQLModel, select
from pathlib import Path
from uuid import UUID

from api.models import Livro

DATABSE_PATH = Path('database.db')
DATABASE_URL = f'sqlite:///{DATABSE_PATH}'
CONNECT_ARGS = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=CONNECT_ARGS)


def criar_db_tabelas():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

livros_deafult_data = [
    {
        "uuid":UUID('f47d6306-6f40-495e-85d3-f06bd70f9f5d'),
        "autor":"George Orwell",
        "titulo":"1994",
        "editora":"Cultura",
        "ano":1949
    },
    {
        "uuid":UUID('a02641bd-c6e5-416f-913a-ac015d65ed3e'),
        "autor":"J. K. Rowling",
        "titulo":"Harry Potter",
        "editora":"Rocco",
        "ano":1997   
    }
]

def adicionar_livros_deafault():
    with Session(engine) as session:
        if not session.exec(select(Livro)).first():
            for data in livros_deafult_data:
                livro = Livro(
                    uuid= data.get('uuid'),
                    autor= data.get('autor'),
                    titulo= data.get('titulo'),
                    editora= data.get('editora'),
                    ano= data.get('ano'),
                )
                session.add(livro)
                session.commit()