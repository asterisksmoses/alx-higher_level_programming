#!/usr/bin/python3

import MySQLdb
import sys

"""THe script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

if __name__ == "__main__":
    """ Tha main entry point of the program."""

    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC LIMIT 1"
    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    cur.close()
    db.close()
