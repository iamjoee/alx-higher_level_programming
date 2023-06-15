#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
Usage: ./14-model_city_fetch_by_state.py <mysql username> /
                                         <mysql password> /
                                         <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{database}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name) \
                   .join(City, City.state_id == State.id) \
                   .order_by(City.id)

    for result in query:
        state_name, city_id, city_name = result
        print(f"{state_name}: ({city_id}) {city_name}")
