#!/usr/bin/python3
"""
contains the class definition of a State and an instance Base = declarative_base():
"""

from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = "states"
    id = Column("id", Integer, primary_key = True, nullable = False, unique = True)
    name = Column("name", String(128), nullable = False)
