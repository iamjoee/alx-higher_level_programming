#!/usr/bin/python3
"""
Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
Safe from SQL injections.
Usage: ./5-filter_cities.py <mysql username> \
                            <mysql password> \
                            <database name> \
                            <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database, state = sys.argv[1:5]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = """
    SELECT c.name
    FROM cities AS c
    INNER JOIN states AS s ON c.state_id = s.id
    WHERE s.name = %s
    ORDER BY c.id
    """

    cursor.execute(query, (state,))
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    db.close()
