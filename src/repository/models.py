from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String

from src.repository.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cpf = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)