#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""

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
    request = "SELECT cities.id, cities.name, states.name FROM cities JOIN states\
    ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(request)

    cityList = cursor.fetchall()

    for city in cityList:
        print(city)

    cursor.close()
    connection.close()
