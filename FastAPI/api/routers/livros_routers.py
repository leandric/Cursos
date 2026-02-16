from fastapi import APIRouter, Depends, HTTPException, Response, Query
from typing import Annotated
from api.models import LivroResposta, Livro, LivroPost, LivroPut, LivroPatch, ConfirmaDelete
from sqlmodel import Session, func, select
from uuid import UUID, uuid4

from api.database import get_session

router = APIRouter(prefix='/livros', tags=['Livros',])

SessionDep = Annotated[Session, Depends(get_session)]

@router.get(path="/", response_model=list[LivroResposta])
async def listar_livros(session: SessionDep, response: Response, page: int = Query(1, ge=1)) -> list[LivroResposta]:
    PAGE_SIZE = 10
    total_items = session.exec(select(func.count()).select_from(Livro)).one()  # type: ignore
    total_pages = (total_items + PAGE_SIZE -1) // PAGE_SIZE

    if page > total_pages and total_pages > 0:
        page = total_pages

    offset = (page -1) * PAGE_SIZE
    query = (
        select(Livro)
        .limit(PAGE_SIZE)
        .offset(offset)
    )

    livros = session.exec(query).all()

    response.headers["X-Total-Pages"] = str(total_pages)
    response.headers["X-Total-Items"] = str(total_items)

    return [LivroResposta.model_validate(livro) for livro in livros]

@router.get('/{livro_id}', response_model=LivroResposta, responses={404: {'description':'Livro não encontrado'}})
async def get_livro(livro_id: UUID, session: SessionDep, ) -> LivroResposta:
    if livro := session.exec(select(Livro).where(Livro.uuid == livro_id)).first():
        return LivroResposta.model_validate(livro)
    raise HTTPException(status_code=404, detail="Livro não encontrado")

    
@router.post("/", response_model=LivroResposta)
async def criar_livro(livro: LivroPost, session: SessionDep) -> LivroResposta:
    novo_uuid = uuid4()

    livro_gerado = Livro(
        uuid=novo_uuid,
        autor=livro.autor,
        titulo=livro.titulo,
        editora=livro.editora,
        ano=livro.ano
    )

    session.add(livro_gerado)
    session.commit()
    return LivroResposta.model_validate(livro_gerado)

@router.put("/{livro_id}", response_model=LivroResposta, responses={404:{'description':'Livro não encontrado'}})
async def atuallizar_livro(livro_id: UUID, livro_update:LivroPut, session: SessionDep) -> LivroResposta:
    if livro := session.exec(select(Livro).where(Livro.uuid == livro_id)).first():
        for key, value in livro_update:
            setattr(livro, key, value)
        session.add(livro)
        session.commit()
        session.refresh(livro)

        return LivroResposta.model_validate(livro)
    raise HTTPException(status_code=404, detail="Livro não encontrado")


@router.patch("/{livro_id}", response_model=LivroResposta, responses={404:{'description':'Livro não encontrado'},
                                                                      400:{'description':'Nenhum dado recebido'}})
async def atuallizar_livro(livro_id: UUID, livro_update:LivroPatch, session: SessionDep) -> LivroResposta:
    update_data = livro_update.model_dump(exclude_unset=True, exclude_none=True)

    if not update_data:
        raise HTTPException(status_code=400, detail='Nenhum dado recebido')
    
    if livro := session.exec(select(Livro).where(Livro.uuid == livro_id)).first():
        for key, value in update_data.items():
            setattr(livro, key, value)

        session.add(livro)
        session.commit()
        session.refresh(livro)
        return LivroResposta.model_validate(livro)
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@router.delete("/{livros_id}", response_model=ConfirmaDelete, responses={404:{'description':'Livro não encontrado'}})
async def deletar_livro(livro_id: UUID, session: SessionDep) -> ConfirmaDelete:
    if livro := session.exec(select(Livro).where(Livro.uuid == livro_id)).first():
            titulo = livro.titulo
            session.delete(livro)
            session.commit()
            return ConfirmaDelete(mensagem=f'Livro {titulo} deletado.', uuid=livro_id)
    
    raise HTTPException(status_code=404, detail='Livro não encontrado')