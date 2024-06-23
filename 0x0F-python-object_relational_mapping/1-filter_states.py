#!/usr/bin/python3

import MySQLdb
import sys

def filt_states(username, password, database):
    """Connect to a MySQL database and filter all states with a name starting with
    upper N.
    Args:
    Username: The MySQL username
    password: The MySQL password
    database: The MySQL database
    """
    try:
        db = MySQLdb.connect(
                host="localhost",
                user=username,
                passwd=password,
                db=database
            )
        cur = db.cursor()

        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
        cur.execute(query)

        res = cur.fetchall()

        for row in res:
            print(row)
    
    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cur.close()
        db.close()
