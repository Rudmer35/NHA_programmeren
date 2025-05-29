import sqlite3

def create_db():
    try:
        sqliteConnection = sqlite3.connect('SQlite_Phyton.db')
        sqlite_create_persoon_querry = """CREATE TABLE IF NOT EXISTS persoon (
        idpersoon INTEGER PRIMARY KEY AUTOINCREMENT,
        voornaam VARCHAR (45) NOT NULL,
        tussenvoegsel VARCHAR(45) NULL,
        achternaam VARCHAR(255) NOT NULL,
        mobiel VARCHAR(23) NOT NULL);"""

        sqlite_create_adres_querry ='''CREATE TABLE IF NOT EXISTS `adres` (
        `idadres` INTEGER PRIMARY KEY AUTOINCREMENT,
        `straat` VARCHAR(45) NOT NULL,
        `huisnr` VARCHAR(45) NOT NULL,
        `postcode` VARCHAR(45) NOT NULL,
        `woonplaats` VARCHAR(45) NOT NULL,
        `idpersoon` INTEGER NOT NULL);'''

        cursor = sqliteConnection.cursor()

        print("Succesfully connected to SQlite")
        cursor.execute(sqlite_create_persoon_querry)
        cursor.execute(sqlite_create_adres_querry)
        sqilteConnection.commit()
        print("SQlite table created")

        cursor.close()
    
    except sqlite3.Error as error:
        return f"Error while creating a sqlite tabel {error}"
    
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            return "SQlite connection is closed"

create_db()
