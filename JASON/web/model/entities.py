from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector


class users(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('cuenta_id_seq'), primary_key=True)
    codigo = Column(String(100))
    nombre = Column(String(100))
    apellido = Column(String(100))
    password = Column(String(100))

