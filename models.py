from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Membros(Base):
    __tablename__ = "membros"

    id_membro = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    celular = Column(Integer,nullable=True)

    assinaturas = relationship("Assinaturas", back_populates="membro")

class Planos(Base):
    __tablename__ = "planos"

    id_plano = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    preco = Column(String, index=True, nullable=False)

    assinaturas = relationship("Assinaturas", back_populates="plano")
    

class Assinaturas(Base):
    __tablename__ = "assinaturas"

    id_assinatura = Column(Integer, primary_key=True, index=True)
    data_ativacao = Column(DateTime, index=True, nullable=False)
    ativo = Column(Integer, index=True, nullable=False)
    id_membro = Column(Integer, ForeignKey("membros.id_membro"))
    id_plano = Column(Integer, ForeignKey("planos.id_plano"))
    
    membro = relationship("Membros", back_populates="assinaturas")
    plano = relationship("Planos", back_populates="assinaturas")