import sqlite3 as sql
import sys
import os.path

listOfTables = ["SettingsGroups", "SettingsPrivateChats", "ExchangeRates", "SettingsExchangeRates"]
_SettingsGroups = [""]

def DbIntegrityCheck():
    if os.path.exists("DataBases/DataForBot.sqlite"):
        #Connect to DB
        con = sql.connect('DataBases/DataForBot.sqlite')
        cursor = con.cursor()

        #Getting all names of tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        listNames = cursor.fetchall()

        cursor.execute("SELECT type FROM sqlite_master WHERE type='table';")
        listTypes = cursor.fetchall()
        for i in cursor.fetchall():
            if not i[0] in listOfTables:
                print("Error. Database is corrupted. Please, delete file 'DataForBot.sqlite'. Delete the file, a new database will be created automatically.")
                sys.exit()
            else:
                print(listTypes)
    else:
        CreateDataBaseTemplate()

def CreateDataBaseTemplate():
    #Connect to DB
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()

    with con:
        con.execute("""
            CREATE TABLE SettingsGroups (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                delete TEXT,
                deleteButton BOOL,
                editSettings TEXT,
                flags BOOL
            );
        """)
    with con:
        con.execute("""
            CREATE TABLE SettingsPrivateChats (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                deleteButton BOOL,
                flags BOOL
            );
        """)
    with con:
        con.execute("""
            CREATE TABLE ExchangeRates (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                currency TEXT,
                flag TEXT,
                exchangeRates FLOAT
            );
        """)
    with con:
        con.execute("""
            CREATE TABLE ExchangeRates (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                AED BOOL,
                AFN BOOL,
                ALL BOOL,
                AMD BOOL,
                ANG BOOL,
                AOA BOOL,
                ARS BOOL,
                AUD BOOL,
                AWG BOOL,
                AZN BOOL,
                BAM BOOL,
                BBD BOOL,
                BDT BOOL,
                BGN BOOL,
                BHD BOOL,
                BIF BOOL,
                BMD BOOL,
                BND BOOL,
                BOB BOOL,
                BRL BOOL,
                BSD BOOL,
                BTC BOOL,
                BTN BOOL,
                BWP BOOL,
                BYN BOOL,
                BYR BOOL,
                BZD BOOL,
                CAD BOOL,
                CDF BOOL,
                CHF BOOL,
                CLF BOOL,
                CLP BOOL,
                CNY BOOL,
                COP BOOL,
                CRC BOOL,
                CUC BOOL,
                CUP BOOL,
                CVE BOOL,
                CZK BOOL,
                DJF BOOL,
                DKK BOOL,
                DOP BOOL,
                DZD BOOL,
                EGP BOOL,
                ERN BOOL,
                ETB BOOL,
                EUR BOOL,
                FJD BOOL,
                FKP BOOL,
                GBP BOOL,
                GEL BOOL,
                GGP BOOL,
                GHS BOOL,
                GIP BOOL,
                GMD BOOL,
                GNF BOOL,
                GTQ BOOL,
                GYD BOOL,
                HKD BOOL,
                HNL BOOL,
                HRK BOOL,
                HTG BOOL,
                HUF BOOL,
                IDR BOOL,
                ILS BOOL,
                IMP BOOL,
                INR BOOL,
                IQD BOOL,
                IRR BOOL,
                ISK BOOL,
                JEP BOOL,
                JMD BOOL,
                JOD BOOL,
                JPY BOOL,
                KES BOOL,
                KGS BOOL,
                KHR BOOL,
                KMF BOOL,
                KPW BOOL,
                KRW BOOL,
                KWD BOOL,
                KYD BOOL,
                KZT BOOL,
                LAK BOOL,
                LBP BOOL,
                LKR BOOL,
                LRD BOOL,
                LSL BOOL,
                LTL BOOL,
                LVL BOOL,
                LYD BOOL,
                MAD BOOL,
                MDL BOOL,
                MGA BOOL,
                MKD BOOL,
                MMK BOOL,
                MNT BOOL,
                MOP BOOL,
                MRO BOOL,
                MUR BOOL,
                MVR BOOL,
                MWK BOOL,
                MXN BOOL,
                MYR BOOL,
                MZN BOOL,
                NAD BOOL,
                NGN BOOL,
                NIO BOOL,
                NOK BOOL,
                NPR BOOL,
                NZD BOOL,
                OMR BOOL,
                PAB BOOL,
                PEN BOOL,
                PGK BOOL,
                PHP BOOL,
                PKR BOOL,
                PLN BOOL,
                PYG BOOL,
                QAR BOOL,
                RON BOOL,
                RSD BOOL,
                RUB BOOL,
                RWF BOOL,
                SAR BOOL,
                SBD BOOL,
                SCR BOOL,
                SDG BOOL,
                SEK BOOL,
                SGD BOOL,
                SHP BOOL,
                SLL BOOL,
                SOS BOOL,
                SRD BOOL,
                STD BOOL,
                SVC BOOL,
                SYP BOOL,
                SZL BOOL,
                THB BOOL,
                TJS BOOL,
                TMT BOOL,
                TND BOOL,
                TOP BOOL,
                TRY BOOL,
                TTD BOOL,
                TWD BOOL,
                TZS BOOL,
                UAH BOOL,
                UGX BOOL,
                USD BOOL,
                UYU BOOL,
                UZS BOOL,
                VEF BOOL,
                VND BOOL,
                VUV BOOL,
                WST BOOL,
                XAF BOOL,
                XAG BOOL,
                XAU BOOL,
                XCD BOOL,
                XDR BOOL,
                XOF BOOL,
                XPF BOOL,
                YER BOOL,
                ZAR BOOL,
                ZMK BOOL,
                ZMW BOOL,
                ZWL BOOL
            );
        """)
    
    con.close()