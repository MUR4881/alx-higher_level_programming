#!/usr/bin/python3

# -*-  encoding: utf-8 -*-

"""
A simple module interacting with a database to fetch data between two
related database table

    Attributes:
    conn: Connection object (connection to the database)
        cur:  cursor (pointer to context) in the database
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1].split()[0], passwd=argv[2],
                           database=argv[3].split()[0])

    cur = conn.cursor()

    cur.execute("SELECT  cities.id,  cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id ORDER BY cities.id"
                )

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
