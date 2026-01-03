from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate
from fastapi_pagination.ext.sqlalchemy import paginate as sqlalchemy_paginate

from app.core.database import SessionLocal
from app.models.atleta import Atleta
from app.schemas.atleta import AtletaCreate, AtletaResponse
from app.repositories.atleta_repository import create_atleta

router = APIRouter(prefix="/atletas", tags=["Atletas"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AtletaResponse)
def criar_atleta(atleta: AtletaCreate, db: Session = Depends(get_db)):
    atleta_db = Atleta(**atleta.dict())
    return create_atleta(db, atleta_db)


@router.get("/", response_model=Page[AtletaResponse])
def listar_atletas(
    nome: str | None = Query(None),
    categoria: str | None = Query(None),
    centro_treinamento: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Atleta)

    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if categoria:
        query = query.filter(Atleta.categoria == categoria)
    if centro_treinamento:
        query = query.filter(Atleta.centro_treinamento == centro_treinamento)

    return sqlalchemy_paginate(query)
