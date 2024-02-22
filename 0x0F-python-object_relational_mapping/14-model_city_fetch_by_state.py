#!/usr/bin/python3
"""City IB classes."""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
import sys


def fetch_cities():
    """City Class."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for state, city in session.query(State, City).\
            filter(City.state_id == State.id).\
            all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()


if __name__ == "__main__":
    fetch_cities()
