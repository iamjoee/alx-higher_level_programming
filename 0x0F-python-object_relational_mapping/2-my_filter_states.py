#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM `states`"
    cursor.execute(query)
    for state in cursor.fetchall():
        print(state)
