#!/usr/bin/python3
"""Deletes a state."""
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def delete_state():
    """
    Deletes all State objects with a name
    containing the letter a in the database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for state in session.query(State).filter(
            State.name.like('%a%')):
        session.delete(state)

    session.commit()
    session.close()


if __name__ == "__main__":
    delete_state()
