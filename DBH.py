import sqlite3 as sql
import sys
import os

listOfTables = ["SettingsGroups", "SettingsPrivateChats", "ExchangeRates", "SettingsExchangeRates", "sqlite_sequence"]
listOfServiceTables = ["AdminsList", "BlackList", "sqlite_sequence"]
#_SettingsGroups = ["chatID", "deleteRules", "deleteButton", "editSettings", "flags"]
#_SettingsPrivateChats = ["chatID", "deleteButton", "flags"]
#_ExchangeRates = ["currency", "flag", "exchangeRates"]

def DbIntegrityCheck():
    if os.path.exists("DataBases/DataForBot.sqlite"):
        #Connect to DB
        con = sql.connect('DataBases/DataForBot.sqlite')
        cursor = con.cursor()
        print("Connected to main DB successfully.")

        #Getting all names of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        listNames = cursor.fetchall()
        for i in range(len(listNames)):
            listNames[i] = listNames[i][0]

        for i in listOfTables:
            if not i in listNames:
                os.remove('DataBases/DataForBot.sqlite')
                print("Error. Main database is corrupted. 'DataForBot.sqlite' was deleted. New database will be create automatically.")
                CreateDataBaseTemplate()
                break
        print("Main DB is OK.")
    else:
        print("Connected to main DB unsuccessfully.")
        CreateDataBaseTemplate()

    if os.path.exists("DataBases/ServiceData.sqlite"):
        #Connect to DB
        con = sql.connect('DataBases/ServiceData.sqlite')
        cursor = con.cursor()
        print("Connected to service DB successfully.")

        #Getting all names of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        listNames = cursor.fetchall()
        for i in range(len(listNames)):
            listNames[i] = listNames[i][0]

        for i in listOfServiceTables:
            if not i in listNames:
                os.remove('DataBases/ServiceData.sqlite')
                print("Error. Service database is corrupted. 'ServiceData.sqlite' was deleted. New database will be create automatically.")
                CreateServiceDataBase()
                break
        print("Service DB is OK.")
    else:
        print("Connected to service DB unsuccessfully.")
        CreateServiceDataBase()

def CreateServiceDataBase():
    print("Creating service DB is starting...")
    #Connect to DB
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()

    with con:
        con.execute("""
            CREATE TABLE AdminsList (
                adminID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
            );
        """)

    with con:
        con.execute("""
            CREATE TABLE BlackList (
                userID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                banDate TEXT,
                chatID INTEGER,
                chatName TEXT
            );
        """)

    con.close()
    print("Service DB is created")

def CreateDataBaseTemplate():
    print("Creating main DB is starting...")
    #Connect to DB
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()

    with con:
        con.execute("""
            CREATE TABLE SettingsGroups (
                chatID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                deleteRules TEXT,
                deleteButton BOOL,
                editSettings TEXT,
                flags BOOL
            );
        """)
    with con:
        con.execute("""
            CREATE TABLE SettingsPrivateChats (
                chatID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                deleteButton BOOL,
                flags BOOL
            );
        """)
    with con:
        con.execute("""
            CREATE TABLE ExchangeRates (
                currency TEXT NOT NULL PRIMARY KEY,
                flag TEXT,
                exchangeRates FLOAT
            );
        """)
    with con:
        con.execute("""
            CREATE TABLE SettingsExchangeRates (
                chatID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                _AED BOOL,
                _AFN BOOL,
                _ALL BOOL,
                _AMD BOOL,
                _ANG BOOL,
                _AOA BOOL,
                _ARS BOOL,
                _AUD BOOL,
                _AWG BOOL,
                _AZN BOOL,
                _BAM BOOL,
                _BBD BOOL,
                _BDT BOOL,
                _BGN BOOL,
                _BHD BOOL,
                _BIF BOOL,
                _BMD BOOL,
                _BND BOOL,
                _BOB BOOL,
                _BRL BOOL,
                _BSD BOOL,
                _BTN BOOL,
                _BWP BOOL,
                _BYN BOOL,
                _BZD BOOL,
                _CAD BOOL,
                _CDF BOOL,
                _CHF BOOL,
                _CLF BOOL,
                _CLP BOOL,
                _CNY BOOL,
                _COP BOOL,
                _CRC BOOL,
                _CUC BOOL,
                _CUP BOOL,
                _CVE BOOL,
                _CZK BOOL,
                _DJF BOOL,
                _DKK BOOL,
                _DOP BOOL,
                _DZD BOOL,
                _EGP BOOL,
                _ERN BOOL,
                _ETB BOOL,
                _EUR BOOL,
                _FJD BOOL,
                _FKP BOOL,
                _GBP BOOL,
                _GEL BOOL,
                _GGP BOOL,
                _GHS BOOL,
                _GIP BOOL,
                _GMD BOOL,
                _GNF BOOL,
                _GTQ BOOL,
                _GYD BOOL,
                _HKD BOOL,
                _HNL BOOL,
                _HRK BOOL,
                _HTG BOOL,
                _HUF BOOL,
                _IDR BOOL,
                _ILS BOOL,
                _IMP BOOL,
                _INR BOOL,
                _IQD BOOL,
                _IRR BOOL,
                _ISK BOOL,
                _JEP BOOL,
                _JMD BOOL,
                _JOD BOOL,
                _JPY BOOL,
                _KES BOOL,
                _KGS BOOL,
                _KHR BOOL,
                _KMF BOOL,
                _KPW BOOL,
                _KRW BOOL,
                _KWD BOOL,
                _KYD BOOL,
                _KZT BOOL,
                _LAK BOOL,
                _LBP BOOL,
                _LKR BOOL,
                _LRD BOOL,
                _LSL BOOL,
                _LTL BOOL,
                _LVL BOOL,
                _LYD BOOL,
                _MAD BOOL,
                _MDL BOOL,
                _MGA BOOL,
                _MKD BOOL,
                _MMK BOOL,
                _MNT BOOL,
                _MOP BOOL,
                _MRO BOOL,
                _MUR BOOL,
                _MVR BOOL,
                _MWK BOOL,
                _MXN BOOL,
                _MYR BOOL,
                _MZN BOOL,
                _NAD BOOL,
                _NGN BOOL,
                _NIO BOOL,
                _NOK BOOL,
                _NPR BOOL,
                _NZD BOOL,
                _OMR BOOL,
                _PAB BOOL,
                _PEN BOOL,
                _PGK BOOL,
                _PHP BOOL,
                _PKR BOOL,
                _PLN BOOL,
                _PYG BOOL,
                _QAR BOOL,
                _RON BOOL,
                _RSD BOOL,
                _RUB BOOL,
                _RWF BOOL,
                _SAR BOOL,
                _SBD BOOL,
                _SCR BOOL,
                _SDG BOOL,
                _SEK BOOL,
                _SGD BOOL,
                _SHP BOOL,
                _SLL BOOL,
                _SOS BOOL,
                _SRD BOOL,
                _STD BOOL,
                _SVC BOOL,
                _SYP BOOL,
                _SZL BOOL,
                _THB BOOL,
                _TJS BOOL,
                _TMT BOOL,
                _TND BOOL,
                _TOP BOOL,
                _TRY BOOL,
                _TTD BOOL,
                _TWD BOOL,
                _TZS BOOL,
                _UAH BOOL,
                _UGX BOOL,
                _USD BOOL,
                _UYU BOOL,
                _UZS BOOL,
                _VEF BOOL,
                _VND BOOL,
                _VUV BOOL,
                _WST BOOL,
                _XAF BOOL,
                _XAG BOOL,
                _XAU BOOL,
                _XCD BOOL,
                _XDR BOOL,
                _XOF BOOL,
                _XPF BOOL,
                _YER BOOL,
                _ZAR BOOL,
                _ZMK BOOL,
                _ZMW BOOL,
                _ZWL BOOL
            );
        """)
    
    con.close()
    print("Main DB is created.")