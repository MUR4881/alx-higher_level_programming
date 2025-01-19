#!/usr/bin/python3

# -*-  encoding: utf-8  -*-

"""
A simple module that queries a database for rows containing a particular value
while being SQL injection save.

This script takes the following argument: username, password, databsename,
the state to filter for.

"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1].split()[0],  password=argv[2],
                           database=argv[3].split()[0])

    cur = conn.cursor()
    cur.execute("SELECT  id, name FROM states WHERE name='%s' ORDER BY id ASC"
                % argv[4].split()[0])

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
