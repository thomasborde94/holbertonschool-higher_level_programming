#!/usr/bin/python3
"""
prints the State object with the name passed as argument
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()
    stateUpdate = session.query(State).filter(State.id == 2).first()
    stateUpdate.name = "New Mexico"
    session.commit()
