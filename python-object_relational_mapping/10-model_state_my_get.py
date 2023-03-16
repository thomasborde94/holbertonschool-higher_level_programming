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
    statename = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == statename).first()

    if states is None:
        print("Not found")
    else:
        for state in states:
            print("{}".format(state.id))
