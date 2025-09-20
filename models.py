from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import declarative_base
from datetime import date

#criando conexão:
db = create_engine("sqlite:///banco.db")

#base do banco:
Base = declarative_base()

#criando classes:
class Veiculo(Base):
    __tablename__ = "veiculo"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    prefixo = Column("prefixo", Integer, nullable=False, unique = True)
    tipo = Column("tipo", String, nullable=False )
    modelo = Column("modelo", String, nullable=False )
    
    def __init__(self, prefixo, tipo, modelo):
        self.prefixo = prefixo
        self.tipo = tipo
        self.modelo = modelo
        

class Retencao(Base):
    __tablename__ = "retencao"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String, nullable=False)
    data_inicial = Column("data_inicial", Date, nullable=False)
    data_retencao = Column("data_retencao", Date, nullable = False)
    dias_retido = Column("dias_retido", Integer, nullable=False)
    garagem = Column("garagem", String, nullable=False)
    prefixo = Column("prefixo", ForeignKey("veiculo.id"))
    
    
    def __init__(self, descricao, data_inicial, data_retencao, dias_retido, garagem, prefixo):
        self.descricao = descricao
        self.data_inicial = data_inicial
        self.data_retencao = data_retencao
        self.dias_retido = dias_retido
        self.garagem = garagem
        self.prefixo = prefixo
        
        
class Usuario(Base):
    __tablename__ = "usuario"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome_usuario = Column("nome_usuario", String, unique = True, nullable=False)
    senha = Column("senha", String, nullable=False)
    admin = Column("admin", Boolean, nullable=False, default=False)
    
    def __init__(self, nome_usuario, senha, admin = False):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.admin = admin
        
        