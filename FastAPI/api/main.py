from contextlib import asynccontextmanager
from fastapi import FastAPI
<<<<<<< HEAD
from api.databse import criar_db_tabelas
=======
<<<<<<< HEAD

from api.database import criar_db_tabelas, adicionar_livros_deafault
=======
from api.databse import criar_db_tabelas
>>>>>>> 15c1cb9 (_+_=_+)
>>>>>>> rescue-detached
from api.routers import livros_routers

@asynccontextmanager
async def lifespan(app: FastAPI):
<<<<<<< HEAD
=======
<<<<<<< HEAD
    # antes
    criar_db_tabelas()
    adicionar_livros_deafault()
    yield
    # depois

app = FastAPI(title="API de Livros", lifespan=lifespan)
=======
>>>>>>> rescue-detached
    criar_db_tabelas()
    yield

app = FastAPI(title="APIde Livros", lifespan=lifespan)

<<<<<<< HEAD
=======
>>>>>>> 15c1cb9 (_+_=_+)
>>>>>>> rescue-detached
app.include_router(livros_routers.router)