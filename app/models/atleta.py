from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base

class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)

    categoria = Column(String)
    centro_treinamento = Column(String)
