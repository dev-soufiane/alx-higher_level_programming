#!/usr/bin/python3
"""Filter states by user input."""
import MySQLdb
import sys


def find_state():
    """
    Display all the states with the given name in the database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database
                         )
    cur = db.cursor()
    cur.execute("""SELECT *\
                FROM states\
                WHERE name LIKE BINARY '{}'\
                ORDER BY id ASC""".format(searched)
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    find_state()
