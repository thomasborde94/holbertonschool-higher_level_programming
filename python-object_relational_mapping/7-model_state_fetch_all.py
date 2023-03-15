#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".\
                           format(username, password, database))

    result = engine.execute(text("SELECT * FROM states;"))
    for row in result.fetchall():
        print(row)

    # New session
    ##Session = sessionmaker(bind=engine)
    ##session = Session()

    
