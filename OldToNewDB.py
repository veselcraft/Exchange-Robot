import sqlite3 as sql
import os
import ast
from DBH import DbIntegrityCheck


DbIntegrityCheck()
if os.path.exists("DataBases/DataForBot.sqlite") and os.path.exists("settings"):
        #Connect to DB
        con = sql.connect('DataBases/DataForBot.sqlite')
        cursor = con.cursor()
        print("Connected to main DB successfully.")
        query = "INSERT OR REPLACE into SettingsExchangeRates (chatID, _AZN,_BYN,_CHF,_CNY,_CZK,_EUR,_GBP,_GEL,_ILS,_INR,_KRW,_KZT,_RUB,_PLN,_UAH,_USD,_UZS) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        query_private = "INSERT OR REPLACE into SettingsPrivateChats (chatID, deleteButton) values (?,?)"
        query_groups = "INSERT OR REPLACE into SettingsGroups (chatID, deleteRules, deleteButton, editSettings) values (?,?,?,?)"
        for filename in os.listdir("settings"):
            with open("settings/"+filename) as f:
                data = f.read()
            data = data.replace("'True'","True")
            data = data.replace("'False'","False")
            d = ast.literal_eval(data)
            d.setdefault("delete_button",0)
            row = (filename[:-5],d.get("AZN"),d.get("BYN"),d.get("CHF"),d.get("CNY"),d.get("CZK"),d.get("EUR"),d.get("GBP"),d.get("GEL"),d.get("ILS"),d.get("INR"),d.get("KRW"),d.get("KZT"),d.get("RUB"),d.get("PLN"),d.get("UAH"),d.get("USD"),d.get("UZS"))
            cursor.execute(query,row)
            if(filename[0]=="-"):
                row = (filename[:-5],d.get("delete"),d.get("delete_button"),d.get("edit"))
                cursor.execute(query_groups,row)
            else:
                row = (filename[:-5],d.get("delete_button"))
                cursor.execute(query_private,row)
        con.commit()
        print("Main DB has been transfered succesfuly")
        if os.path.exists("logs"):
            con = sql.connect('DataBases/ServiceData.sqlite')
            cursor = con.cursor()
            print("Connected to service DB successfully.")
            with open("logs/black_list.ertb") as f:
                data = f.read().splitlines()
                data = [tuple([k]) for k in data]
                print(data)
            cursor.executemany("INSERT OR REPLACE INTO BlackList (userID,banDate) values (?,DATE())",data)
            con.commit()
            print("Blacklist was succesfuly transfered")
        else:
            print("Transfering blacklist has failed. Logs were not found")




else:
    print("DB or settings not found")
