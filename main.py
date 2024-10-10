import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# CREATE DATABASE meubanco

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

# Criando tabela.
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    
    def __init__(self, nome: str, email: str, senha: str) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha

Base.metadata.create_all(bind=db)   

usuario = Usuario(nome="Marta", email="marta@gmail.com", senha="123")
session.add(usuario)
session.commit()

lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")


