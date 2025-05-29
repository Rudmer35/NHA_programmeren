import sqlite3

def insert_persoon():
    try:
        sqliteConnection = sqlite3.connect('SQlite_Phyton.db')
        insert_persoon_query = ''' INSERT INTO persoon(voornaam, tussenvoegsel, achternaam, mobiel)
        VALUES ('jan', '', 'jansen', '064334544');'''

        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")
        cursor.execute(insert_persoon_query)
        sqliteConnection.commit()
        print("Persoon ingevoerd")

        cursor.close()
    
    except sqlite3.Error as error:
        print(f"Persoon niet ingevoerd :\n {error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
        
        return "sqlite connection is closed"

insert_persoon()