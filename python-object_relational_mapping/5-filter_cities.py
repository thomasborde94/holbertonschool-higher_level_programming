#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all
cities of that state"""

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
    request = "SELECT cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC"
    infos = (statename,)
    cursor.execute(request, infos)

    cityList = cursor.fetchall()

    print(", ".join(city[0] for city in cityList))

    cursor.close()
    connection.close()
