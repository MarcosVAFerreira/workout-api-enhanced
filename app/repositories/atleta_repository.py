from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.atleta import Atleta
from fastapi import HTTPException, status

def create_atleta(db: Session, atleta: Atleta):
    try:
        db.add(atleta)
        db.commit()
        db.refresh(atleta)
        return atleta
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}"
        )
