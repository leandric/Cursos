from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.database import criar_db_tabelas, adicionar_livros_deafault
from api.routers import livros_routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    # antes
    criar_db_tabelas()
    adicionar_livros_deafault()
    yield
    # depois

app = FastAPI(title="API de Livros", lifespan=lifespan)
app.include_router(livros_routers.router)