#!/usr/bin/python3
"""  lists all states with a name starting with N"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    connection = MySQLdb.connect(user=username, passwd=password,
                                 db=database, host="localhost",
                                 port=3306)

    cursor = connection.cursor()
    request = "SELECT * FROM states WHERE name LIKE '%N%' ORDER BY states.id"
    cursor.execute(request)

    stateList = cursor.fetchall()

    for state in stateList:
        print(state)

    cursor.close()
    connection.close()
