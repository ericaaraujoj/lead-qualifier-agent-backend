from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Este é o caminho DENTRO do container, que aponta para o volume do Docker.
DATABASE_URL = "sqlite:////data/agente.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} # check_same_thread é necessário para SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 2. Este é o "molde" da nossa tabela de Serviços
class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String) # Adicionamos a descrição
    duracao_minutos = Column(Integer)

# 3. Esta linha é o que efetivamente cria a tabela (e o arquivo agente.db)
Base.metadata.create_all(bind=engine)