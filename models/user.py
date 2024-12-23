from db import Base
from sqlalchemy import Column, String, Integer


class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    role = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)
    image = Column(String(255), nullable=True)



