from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List

# Importa o Pydantic
from pydantic import BaseModel 

# Importa nossas configurações de banco e o modelo
from app import database
from app database import Servico, SessionLocal, engine # Garanta que 'engine' está importado

# Cria as tabelas (se não existirem)
database.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Agente de Agendamento")

class ServicoCreate(BaseModel):
    nome: str
    descricao: str
    duracao_minutos: int

class ServicoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    duracao_minutos: int

    class Config:
        orm_mode = True    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()        

@app.post("/api/servicos", response_model=ServicoResponse)
def criar_servico(servico: ServicoCreate, db: Session = Depends(get_db)):
    # Cria um objeto SQLAlchemy a partir do Pydantic
    db_servico = Servico(
        nome=servico.nome,
        descricao=servico.descricao,
        duracao_minutos=servico.duracao_minutos
    )
    db.add(db_servico)
    db.commit()
    db.refresh(db_servico)
    return db_servico        

app.mount("/", StaticFiles(directory="admin", html=True), name="admin")    