#!/usr/bin/python3

""" This script lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

def list_states(username, password, database):
    """ Connects to a MySQL server and lists all the states from the database hbtn_0e_0_usa.
    Args:
    username: The MySQL username
    password: The MySQL password
    database: The name of the MySQL database
    """
    if __name__ == "__main__":
        db = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                port=3306
            )

        cursor = db.cursor()
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        
        results = cursor.fetchall()
        for row in results:
            print (row)

        cursor.close()
        db.close()
