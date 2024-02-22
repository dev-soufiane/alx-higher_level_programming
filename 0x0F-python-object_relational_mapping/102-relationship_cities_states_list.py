#!/usr/bin/python3
"""State city module."""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
import sys


def fetch_city_state():
    """Gets all states cities in database."""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.commit()
    session.close()


if __name__ == "__main__":
    fetch_city_state()
