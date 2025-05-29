import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLITE_PHYTON.db')
    cursor = sqilteConnection.cursor()
    printJ('Database created and succesfully connected to SQlite')

    sqlite_select_Query = 'select sqlite_versionJ();'
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print('SQlite database version is : ', record)
    cursor.close()
except sqlite3.Error as error:
    print('Error while connecting to sqlite', error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('The SQlite connection is closed')