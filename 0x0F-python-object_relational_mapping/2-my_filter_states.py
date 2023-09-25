#!/usr/bin/python3
"""a script that takes in an argument and displays all
values in the states table
of hbtn_0e_0_usa where name matches the argument."""

if __name__ == "__main__":

    import MySQLdb
    import sys

    args = sys.argv
    mysql_username = args[1]
    mysql_password = args[2]
    database_name = args[3]
    state_name_searched = args[4]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        charset="utf8",
    )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT *\
        FROM states\
        WHERE states.name LIKE BINARY '{}%'\
        ORDER BY id ASC".format(
            state_name_searched
        )
    )

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    connection.close()
