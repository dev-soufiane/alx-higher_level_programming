#!/usr/bin/python3
"""Update a State."""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def update_state():
    """
    Changes the name of a State in the database.
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
    session.query(State).filter_by(id=2).\
        update({State.name: 'New Mexico'}, synchronize_session=False)
    session.commit()
    session.close()


if __name__ == "__main__":
    update_state()
