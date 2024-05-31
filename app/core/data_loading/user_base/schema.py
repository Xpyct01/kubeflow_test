from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    type = Column(String)


class Document(Base):
    __tablename__ = 'Document'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
