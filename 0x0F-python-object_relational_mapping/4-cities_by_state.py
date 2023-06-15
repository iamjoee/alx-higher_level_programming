#!/usr/bin/python3
"""
Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
Usage: ./4-cities_by_state.py <mysql username> \
                            <mysql password> \
                            <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = """
    SELECT c.id, c.name, s.name
    FROM cities AS c
    INNER JOIN states AS s ON c.state_id = s.id
    ORDER BY c.id
    """

    cursor.execute(query)
    cities = cursor.fetchall()
    [print(city) for city in cities]

    cursor.close()
    db.close()
