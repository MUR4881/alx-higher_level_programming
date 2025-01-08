#!/usr/bin/python3

# -*- encoding: utf-8 -*-

"""
A simple module/script that interacts with a database
This, script accepts the following arguements: mysql username, mysql password
and database name.

simple, therefore no argument validation!

    Attributes:
        conn: connection object to the database
         cur: cursor object to the database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")

    for row in cur.fetchall():
        print(row)
