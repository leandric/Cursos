from pydantic import BaseModel
from sqlmodel import Field, SQLModel
<<<<<<< HEAD
=======
<<<<<<< HEAD
from uuid import uuid4, UUID


class LivroBase(SQLModel):
=======
>>>>>>> rescue-detached
from uuid import UUID, uuid4


class LivrosBase(SQLModel):
<<<<<<< HEAD
=======
>>>>>>> 15c1cb9 (_+_=_+)
>>>>>>> rescue-detached
    autor: str = Field(index=True)
    titulo: str = Field(index=True)
    editora: str = Field(index=True)
    ano: int = Field(index=True)


<<<<<<< HEAD
class Livro(LivrosBase, table=True):
=======
<<<<<<< HEAD
class Livro(LivroBase, table=True):
=======
class Livro(LivrosBase, table=True):
>>>>>>> 15c1cb9 (_+_=_+)
>>>>>>> rescue-detached
    id: int | None = Field(default=None, primary_key=True)
    uuid: UUID = Field(default_factory=uuid4, unique=True)


<<<<<<< HEAD
=======
<<<<<<< HEAD
class LivroResposta(LivroBase):
    uuid: UUID


class LivroPost(LivroBase):
    ...


class LivroPut(LivroBase):
=======
>>>>>>> rescue-detached
class LivroResposta(LivrosBase):
    uuid: UUID


class LivroPost(LivrosBase):
    ...


class LivroPut(LivrosBase):
<<<<<<< HEAD
=======
>>>>>>> 15c1cb9 (_+_=_+)
>>>>>>> rescue-detached
    ...


class LivroPatch(SQLModel):
<<<<<<< HEAD
=======
<<<<<<< HEAD
    autor: str | None = None
    titulo: str | None = None
    editora:str | None = None
    ano: int | None = None
=======
>>>>>>> rescue-detached
    autor: str| None = None
    titulo: str| None = None
    editora: str| None = None
    ano: int| None = None
<<<<<<< HEAD
=======
>>>>>>> 15c1cb9 (_+_=_+)
>>>>>>> rescue-detached


class ConfirmaDelete(BaseModel):
    mensagem: str
    uuid: UUID