#!/usr/bin/python3
"""All cities by state."""
import MySQLdb
import sys


def find_cities():
    """
    Gets name of a state and lists all cities
    of that state in the database.
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
    cur.execute("SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %(state_name)s\
                ORDER BY cities.id ASC",
                {'state_name': searched}
                )
    rows = cur.fetchall()
    lst = []
    for row in rows:
        for col in row:
            lst.append(col)
    print(', '.join(lst))
    cur.close()
    db.close()


if __name__ == "__main__":
    find_cities()
