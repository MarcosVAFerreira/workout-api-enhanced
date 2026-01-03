from pydantic import BaseModel

class AtletaCreate(BaseModel):
    nome: str
    cpf: str
    categoria: str
    centro_treinamento: str


class AtletaResponse(BaseModel):
    nome: str
    categoria: str
    centro_treinamento: str

    class Config:
        orm_mode = True
