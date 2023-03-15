#!/usr/bin/python3
"""
contains the class definition of a State and an instance Base:
"""
from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    defines State class:
    id: id of the state
    name: name of the state
    """
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True, nullable=False, unique=True)
    name = Column("name", String(128), nullable=False)
