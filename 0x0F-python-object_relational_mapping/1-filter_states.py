#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    """Connect to a MySQL database and filter all states with a name starting with
    upper N.
    Args:
    Username: The MySQL username
    password: The MySQL password
    database: The MySQL database
    """

    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

    cur = db.cursor()

    query = """
    SELECT MIN(states.id), states.name
    FROM states
    WHERE states.name LIKE BINARY 'N%'
    GROUP BY states.name
    ORDER BY MIN(states.id)
    """

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
