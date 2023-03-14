#!/usr/bin/python3
""" takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]
    connection = MySQLdb.connect(user=username, passwd=password,
                                 db=database, host="localhost",
                                 port=3306)
    cursor = connection.cursor()

    request = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    infos = (statename,)
    cursor.execute(request, infos)

    stateList = cursor.fetchall()

    for state in stateList:
        print(state)

    cursor.close()
    connection.close()
