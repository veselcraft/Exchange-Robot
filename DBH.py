import sqlite3 as sql
import sys
import os.path

listOfTables = ["SettingsGroups", "SettingsPrivateChats", "ExchangeRates", "SettingsExchangeRates"]

def DbIntegrityCheck():
    if os.path.exists("DataBases/DataForBot.sqlite"):
        #Connect to DB
        con = sql.connect('DataBases/DataForBot.sqlite')
        cursor = con.cursor()

        #Getting all names of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for i in cursor.fetchall():
            if not i[0] in listOfTables:
                print("Error. Database is corrupted. Please, delete file 'DataForBot.sqlite'. Delete the file, a new database will be created automatically.")
                sys.exit()
    else:
        #Connect to DB
        con = sql.connect('DataBases/DataForBot.sqlite')
        cursor = con.cursor()
    

    

    with con:
        con.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            );
        """)

    with con:
        con.execute("""
            CREATE TABLE LOL (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            );
        """)

    with con:
        con.execute("""
            CREATE TABLE LOL3 (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            );
        """)
    con.close()