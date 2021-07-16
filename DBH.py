import sqlite3 as sql
import sys
import os
from typing import Set
import json

listOfTables = ["SettingsGroups", "SettingsPrivateChats", "ExchangeRates", "SettingsExchangeRates","CryptoRates","SettingsCryptoRates"]
listOfServiceTables = ["AdminsList", "BlackList","Reports"]
listOfStatsTables = ["ChatsTimeStats","ChatsUsage","ProcessedCurrencies"]

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

    if os.path.exists("DataBases/StatsData.sqlite"):
        con = sql.connect("DataBases/StatsData.sqlite")
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        listNames = cursor.fetchall()
        for i in range(len(listNames)):
            listNames[i]=listNames[i][0]
        
        for i in listOfStatsTables:
            if not i in listNames:
                os.remove("DataBases/StatsData.sqlite")
                print("Error. Stats database is corrupted. 'StatsData.sqlite' was deleted. New database will be create automatically.")
                CreateStatsDataBase()
                break
        print("Stats DB is OK.")
    else:
        print("Connected to stats DB unsuccessfully.")
        CreateStatsDataBase()


def CreateStatsDataBase():
    print("Creating stats DB is starting...")
    #Connect to DB
    con = sql.connect('DataBases/StatsData.sqlite')
    cursor = con.cursor()

    with con:
        con.execute("""
            CREATE TABLE ChatsUsage (
                chatID INTEGER NOT NULL PRIMARY KEY,
                chatType TEXT,
                timeAdded TEXT,
                lastTimeUse TEXT
            );
        """)

    with con:
        con.execute("""
            CREATE TABLE ChatsTimeStats (
                date TEXT,
                privateChatsAmount INTEGER DEFAULT 0,
                groupChatsAmount INTEGER DEFAULT 0,
                activeWeekPrivateChats INTEGER DEFAULT 0,
                activeWeekGroupChats INTEGER DEFAULT 0,
                activeMonthPrivateChats INTEGER DEFAULT 0,
                activeMonthGroupChats INTEGER DEFAULT 0
            );
        """)
    
    with con:
        con.execute("""
            CREATE TABLE ProcessedCurrencies (
                date TEXT,
                chatID INTEGER,
                userID INTEGER,
                proccesedCurrency TEXT,
                message TEXT,
                _AED INTEGER DEFAULT 0,
                _AFN INTEGER DEFAULT 0,
                _ALL INTEGER DEFAULT 0,
                _AMD INTEGER DEFAULT 0,
                _ANG INTEGER DEFAULT 0,
                _AOA INTEGER DEFAULT 0,
                _ARS INTEGER DEFAULT 0,
                _AUD INTEGER DEFAULT 0,
                _AWG INTEGER DEFAULT 0,
                _AZN INTEGER DEFAULT 0,
                _BAM INTEGER DEFAULT 0,
                _BBD INTEGER DEFAULT 0,
                _BDT INTEGER DEFAULT 0,
                _BGN INTEGER DEFAULT 0,
                _BHD INTEGER DEFAULT 0,
                _BIF INTEGER DEFAULT 0,
                _BMD INTEGER DEFAULT 0,
                _BND INTEGER DEFAULT 0,
                _BOB INTEGER DEFAULT 0,
                _BRL INTEGER DEFAULT 0,
                _BSD INTEGER DEFAULT 0,
                _BTN INTEGER DEFAULT 0,
                _BWP INTEGER DEFAULT 0,
                _BYN INTEGER DEFAULT 0,
                _BZD INTEGER DEFAULT 0,
                _CAD INTEGER DEFAULT 0,
                _CDF INTEGER DEFAULT 0,
                _CHF INTEGER DEFAULT 0,
                _CLF INTEGER DEFAULT 0,
                _CLP INTEGER DEFAULT 0,
                _CNY INTEGER DEFAULT 0,
                _COP INTEGER DEFAULT 0,
                _CRC INTEGER DEFAULT 0,
                _CUC INTEGER DEFAULT 0,
                _CUP INTEGER DEFAULT 0,
                _CVE INTEGER DEFAULT 0,
                _CZK INTEGER DEFAULT 0,
                _DJF INTEGER DEFAULT 0,
                _DKK INTEGER DEFAULT 0,
                _DOP INTEGER DEFAULT 0,
                _DZD INTEGER DEFAULT 0,
                _EGP INTEGER DEFAULT 0,
                _ERN INTEGER DEFAULT 0,
                _ETB INTEGER DEFAULT 0,
                _EUR INTEGER DEFAULT 0,
                _FJD INTEGER DEFAULT 0,
                _FKP INTEGER DEFAULT 0,
                _GBP INTEGER DEFAULT 0,
                _GEL INTEGER DEFAULT 0,
                _GGP INTEGER DEFAULT 0,
                _GHS INTEGER DEFAULT 0,
                _GIP INTEGER DEFAULT 0,
                _GMD INTEGER DEFAULT 0,
                _GNF INTEGER DEFAULT 0,
                _GTQ INTEGER DEFAULT 0,
                _GYD INTEGER DEFAULT 0,
                _HKD INTEGER DEFAULT 0,
                _HNL INTEGER DEFAULT 0,
                _HRK INTEGER DEFAULT 0,
                _HTG INTEGER DEFAULT 0,
                _HUF INTEGER DEFAULT 0,
                _IDR INTEGER DEFAULT 0,
                _ILS INTEGER DEFAULT 0,
                _IMP INTEGER DEFAULT 0,
                _INR INTEGER DEFAULT 0,
                _IQD INTEGER DEFAULT 0,
                _IRR INTEGER DEFAULT 0,
                _ISK INTEGER DEFAULT 0,
                _JEP INTEGER DEFAULT 0,
                _JMD INTEGER DEFAULT 0,
                _JOD INTEGER DEFAULT 0,
                _JPY INTEGER DEFAULT 0,
                _KES INTEGER DEFAULT 0,
                _KGS INTEGER DEFAULT 0,
                _KHR INTEGER DEFAULT 0,
                _KMF INTEGER DEFAULT 0,
                _KPW INTEGER DEFAULT 0,
                _KRW INTEGER DEFAULT 0,
                _KWD INTEGER DEFAULT 0,
                _KYD INTEGER DEFAULT 0,
                _KZT INTEGER DEFAULT 0,
                _LAK INTEGER DEFAULT 0,
                _LBP INTEGER DEFAULT 0,
                _LKR INTEGER DEFAULT 0,
                _LRD INTEGER DEFAULT 0,
                _LSL INTEGER DEFAULT 0,
                _LTL INTEGER DEFAULT 0,
                _LVL INTEGER DEFAULT 0,
                _LYD INTEGER DEFAULT 0,
                _MAD INTEGER DEFAULT 0,
                _MDL INTEGER DEFAULT 0,
                _MGA INTEGER DEFAULT 0,
                _MKD INTEGER DEFAULT 0,
                _MMK INTEGER DEFAULT 0,
                _MNT INTEGER DEFAULT 0,
                _MOP INTEGER DEFAULT 0,
                _MRO INTEGER DEFAULT 0,
                _MUR INTEGER DEFAULT 0,
                _MVR INTEGER DEFAULT 0,
                _MWK INTEGER DEFAULT 0,
                _MXN INTEGER DEFAULT 0,
                _MYR INTEGER DEFAULT 0,
                _MZN INTEGER DEFAULT 0,
                _NAD INTEGER DEFAULT 0,
                _NGN INTEGER DEFAULT 0,
                _NIO INTEGER DEFAULT 0,
                _NOK INTEGER DEFAULT 0,
                _NPR INTEGER DEFAULT 0,
                _NZD INTEGER DEFAULT 0,
                _OMR INTEGER DEFAULT 0,
                _PAB INTEGER DEFAULT 0,
                _PEN INTEGER DEFAULT 0,
                _PGK INTEGER DEFAULT 0,
                _PHP INTEGER DEFAULT 0,
                _PKR INTEGER DEFAULT 0,
                _PLN INTEGER DEFAULT 0,
                _PYG INTEGER DEFAULT 0,
                _QAR INTEGER DEFAULT 0,
                _RON INTEGER DEFAULT 0,
                _RSD INTEGER DEFAULT 0,
                _RUB INTEGER DEFAULT 0,
                _RWF INTEGER DEFAULT 0,
                _SAR INTEGER DEFAULT 0,
                _SBD INTEGER DEFAULT 0,
                _SCR INTEGER DEFAULT 0,
                _SDG INTEGER DEFAULT 0,
                _SEK INTEGER DEFAULT 0,
                _SGD INTEGER DEFAULT 0,
                _SHP INTEGER DEFAULT 0,
                _SLL INTEGER DEFAULT 0,
                _SOS INTEGER DEFAULT 0,
                _SRD INTEGER DEFAULT 0,
                _SVC INTEGER DEFAULT 0,
                _SYP INTEGER DEFAULT 0,
                _SZL INTEGER DEFAULT 0,
                _THB INTEGER DEFAULT 0,
                _TJS INTEGER DEFAULT 0,
                _TMT INTEGER DEFAULT 0,
                _TND INTEGER DEFAULT 0,
                _TOP INTEGER DEFAULT 0,
                _TRY INTEGER DEFAULT 0,
                _TTD INTEGER DEFAULT 0,
                _TWD INTEGER DEFAULT 0,
                _TZS INTEGER DEFAULT 0,
                _UAH INTEGER DEFAULT 0,
                _UGX INTEGER DEFAULT 0,
                _USD INTEGER DEFAULT 0,
                _UYU INTEGER DEFAULT 0,
                _UZS INTEGER DEFAULT 0,
                _VEF INTEGER DEFAULT 0,
                _VND INTEGER DEFAULT 0,
                _VUV INTEGER DEFAULT 0,
                _WST INTEGER DEFAULT 0,
                _XAF INTEGER DEFAULT 0,
                _XAG INTEGER DEFAULT 0,
                _XAU INTEGER DEFAULT 0,
                _XCD INTEGER DEFAULT 0,
                _XOF INTEGER DEFAULT 0,
                _XPF INTEGER DEFAULT 0,
                _YER INTEGER DEFAULT 0,
                _ZAR INTEGER DEFAULT 0,
                _ZMW INTEGER DEFAULT 0,
                _ZWL INTEGER DEFAULT 0,
                ADA INTEGER DEFAULT 0,
                BCH INTEGER DEFAULT 0,
                BNB INTEGER DEFAULT 0,
                BTC INTEGER DEFAULT 0,
                DASH INTEGER DEFAULT 0,
                DOGE INTEGER DEFAULT 0,
                ETC INTEGER DEFAULT 0,
                ETH INTEGER DEFAULT 0,
                LTC INTEGER DEFAULT 0,
                RVN INTEGER DEFAULT 0,
                TRX INTEGER DEFAULT 0,
                XLM INTEGER DEFAULT 0,
                XMR INTEGER DEFAULT 0,
                XRP INTEGER DEFAULT 0
            );
        """)

    con.close()
    print("Stats DB is created")

def CreateServiceDataBase():
    if os.path.exists("DataBases"):
        pass
    else:
        print("Folder 'DataBases' not found")
        sys.exit(1)
    print("Creating service DB is starting...")
    #Connect to DB
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()

    with con:
        con.execute("""
            CREATE TABLE AdminsList (
                adminID INTEGER NOT NULL PRIMARY KEY 
            );
        """)

    with con:
        con.execute("""
            CREATE TABLE BlackList (
                userID INTEGER NOT NULL PRIMARY KEY ,
                banDate TEXT DEFAULT 0,
                chatID INTEGER DEFAULT 0,
                chatName TEXT DEFAULT 0
            );
        """)
    
    with con:
        con.execute("""
            CREATE TABLE Reports (
                date TEXT,
                chatID INTEGER DEFAULT 0,
                userID INTEGER DEFAULT 0,
                message TEXT,
                reply TEXT
            );
        """)

    con.close()
    print("Service DB is created")

def CreateDataBaseTemplate():
    if os.path.exists("DataBases"):
        pass
    else:
        print("Folder 'DataBases' not found")
        os.mkdir("DataBases")
        print("Folder 'DataBases' is created")
    print("Creating main DB is starting...")
    #Connect to DB
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()

    with con:
        con.execute("""
            CREATE TABLE SettingsGroups (
                chatID INTEGER NOT NULL PRIMARY KEY ,
                deleteRules TEXT DEFAULT admins,
                deleteButton INTEGER DEFAULT 1,
                editSettings TEXT DEFAULT admins,
                flags INTEGER DEFAULT 1,
                lang TEXT DEFAULT en
            );
        """)
    with con:
        con.execute("""
            CREATE TABLE SettingsPrivateChats (
                chatID INTEGER NOT NULL PRIMARY KEY ,
                deleteButton INTEGER DEFAULT 1,
                flags INTEGER DEFAULT 1,
                lang TEXT DEFAULT en
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
            CREATE TABLE CryptoRates (
                currency TEXT NOT NULL PRIMARY KEY,
                flag TEXT,
                exchangeRates FLOAT
            );
        """)
    
    with con:
        con.execute("""
            CREATE TABLE SettingsCryptoRates (
                chatID INTEGER NOT NULL PRIMARY KEY,
                ADA INTEGER DEFAULT 0,
                BCH INTEGER DEFAULT 0,
                BNB INTEGER DEFAULT 0,
                BTC INTEGER DEFAULT 0,
                DASH INTEGER DEFAULT 0,
                DOGE INTEGER DEFAULT 0,
                ETC INTEGER DEFAULT 0,
                ETH INTEGER DEFAULT 0,
                LTC INTEGER DEFAULT 0,
                RVN INTEGER DEFAULT 0,
                TRX INTEGER DEFAULT 0,
                XLM INTEGER DEFAULT 0,
                XMR INTEGER DEFAULT 0,
                XRP INTEGER DEFAULT 0  
            );
        """)
    
    with con:
        con.execute("""
            CREATE TABLE SettingsExchangeRates (
                chatID INTEGER NOT NULL PRIMARY KEY ,
                _AED INTEGER DEFAULT 0,
                _AFN INTEGER DEFAULT 0,
                _ALL INTEGER DEFAULT 0,
                _AMD INTEGER DEFAULT 0,
                _ANG INTEGER DEFAULT 0,
                _AOA INTEGER DEFAULT 0,
                _ARS INTEGER DEFAULT 0,
                _AUD INTEGER DEFAULT 0,
                _AWG INTEGER DEFAULT 0,
                _AZN INTEGER DEFAULT 0,
                _BAM INTEGER DEFAULT 0,
                _BBD INTEGER DEFAULT 0,
                _BDT INTEGER DEFAULT 0,
                _BGN INTEGER DEFAULT 0,
                _BHD INTEGER DEFAULT 0,
                _BIF INTEGER DEFAULT 0,
                _BMD INTEGER DEFAULT 0,
                _BND INTEGER DEFAULT 0,
                _BOB INTEGER DEFAULT 0,
                _BRL INTEGER DEFAULT 0,
                _BSD INTEGER DEFAULT 0,
                _BTN INTEGER DEFAULT 0,
                _BWP INTEGER DEFAULT 0,
                _BYN INTEGER DEFAULT 0,
                _BZD INTEGER DEFAULT 0,
                _CAD INTEGER DEFAULT 0,
                _CDF INTEGER DEFAULT 0,
                _CHF INTEGER DEFAULT 0,
                _CLF INTEGER DEFAULT 0,
                _CLP INTEGER DEFAULT 0,
                _CNY INTEGER DEFAULT 0,
                _COP INTEGER DEFAULT 0,
                _CRC INTEGER DEFAULT 0,
                _CUC INTEGER DEFAULT 0,
                _CUP INTEGER DEFAULT 0,
                _CVE INTEGER DEFAULT 0,
                _CZK INTEGER DEFAULT 0,
                _DJF INTEGER DEFAULT 0,
                _DKK INTEGER DEFAULT 0,
                _DOP INTEGER DEFAULT 0,
                _DZD INTEGER DEFAULT 0,
                _EGP INTEGER DEFAULT 0,
                _ERN INTEGER DEFAULT 0,
                _ETB INTEGER DEFAULT 0,
                _EUR INTEGER DEFAULT 1,
                _FJD INTEGER DEFAULT 0,
                _FKP INTEGER DEFAULT 0,
                _GBP INTEGER DEFAULT 1,
                _GEL INTEGER DEFAULT 0,
                _GGP INTEGER DEFAULT 0,
                _GHS INTEGER DEFAULT 0,
                _GIP INTEGER DEFAULT 0,
                _GMD INTEGER DEFAULT 0,
                _GNF INTEGER DEFAULT 0,
                _GTQ INTEGER DEFAULT 0,
                _GYD INTEGER DEFAULT 0,
                _HKD INTEGER DEFAULT 0,
                _HNL INTEGER DEFAULT 0,
                _HRK INTEGER DEFAULT 0,
                _HTG INTEGER DEFAULT 0,
                _HUF INTEGER DEFAULT 0,
                _IDR INTEGER DEFAULT 0,
                _ILS INTEGER DEFAULT 0,
                _IMP INTEGER DEFAULT 0,
                _INR INTEGER DEFAULT 0,
                _IQD INTEGER DEFAULT 0,
                _IRR INTEGER DEFAULT 0,
                _ISK INTEGER DEFAULT 0,
                _JEP INTEGER DEFAULT 0,
                _JMD INTEGER DEFAULT 0,
                _JOD INTEGER DEFAULT 0,
                _JPY INTEGER DEFAULT 0,
                _KES INTEGER DEFAULT 0,
                _KGS INTEGER DEFAULT 0,
                _KHR INTEGER DEFAULT 0,
                _KMF INTEGER DEFAULT 0,
                _KPW INTEGER DEFAULT 0,
                _KRW INTEGER DEFAULT 0,
                _KWD INTEGER DEFAULT 0,
                _KYD INTEGER DEFAULT 0,
                _KZT INTEGER DEFAULT 0,
                _LAK INTEGER DEFAULT 0,
                _LBP INTEGER DEFAULT 0,
                _LKR INTEGER DEFAULT 0,
                _LRD INTEGER DEFAULT 0,
                _LSL INTEGER DEFAULT 0,
                _LTL INTEGER DEFAULT 0,
                _LVL INTEGER DEFAULT 0,
                _LYD INTEGER DEFAULT 0,
                _MAD INTEGER DEFAULT 0,
                _MDL INTEGER DEFAULT 0,
                _MGA INTEGER DEFAULT 0,
                _MKD INTEGER DEFAULT 0,
                _MMK INTEGER DEFAULT 0,
                _MNT INTEGER DEFAULT 0,
                _MOP INTEGER DEFAULT 0,
                _MRO INTEGER DEFAULT 0,
                _MUR INTEGER DEFAULT 0,
                _MVR INTEGER DEFAULT 0,
                _MWK INTEGER DEFAULT 0,
                _MXN INTEGER DEFAULT 0,
                _MYR INTEGER DEFAULT 0,
                _MZN INTEGER DEFAULT 0,
                _NAD INTEGER DEFAULT 0,
                _NGN INTEGER DEFAULT 0,
                _NIO INTEGER DEFAULT 0,
                _NOK INTEGER DEFAULT 0,
                _NPR INTEGER DEFAULT 0,
                _NZD INTEGER DEFAULT 0,
                _OMR INTEGER DEFAULT 0,
                _PAB INTEGER DEFAULT 0,
                _PEN INTEGER DEFAULT 0,
                _PGK INTEGER DEFAULT 0,
                _PHP INTEGER DEFAULT 0,
                _PKR INTEGER DEFAULT 0,
                _PLN INTEGER DEFAULT 0,
                _PYG INTEGER DEFAULT 0,
                _QAR INTEGER DEFAULT 0,
                _RON INTEGER DEFAULT 0,
                _RSD INTEGER DEFAULT 0,
                _RUB INTEGER DEFAULT 0,
                _RWF INTEGER DEFAULT 0,
                _SAR INTEGER DEFAULT 0,
                _SBD INTEGER DEFAULT 0,
                _SCR INTEGER DEFAULT 0,
                _SDG INTEGER DEFAULT 0,
                _SEK INTEGER DEFAULT 0,
                _SGD INTEGER DEFAULT 0,
                _SHP INTEGER DEFAULT 0,
                _SLL INTEGER DEFAULT 0,
                _SOS INTEGER DEFAULT 0,
                _SRD INTEGER DEFAULT 0,
                _SVC INTEGER DEFAULT 0,
                _SYP INTEGER DEFAULT 0,
                _SZL INTEGER DEFAULT 0,
                _THB INTEGER DEFAULT 0,
                _TJS INTEGER DEFAULT 0,
                _TMT INTEGER DEFAULT 0,
                _TND INTEGER DEFAULT 0,
                _TOP INTEGER DEFAULT 0,
                _TRY INTEGER DEFAULT 0,
                _TTD INTEGER DEFAULT 0,
                _TWD INTEGER DEFAULT 0,
                _TZS INTEGER DEFAULT 0,
                _UAH INTEGER DEFAULT 1,
                _UGX INTEGER DEFAULT 0,
                _USD INTEGER DEFAULT 1,
                _UYU INTEGER DEFAULT 0,
                _UZS INTEGER DEFAULT 0,
                _VEF INTEGER DEFAULT 0,
                _VND INTEGER DEFAULT 0,
                _VUV INTEGER DEFAULT 0,
                _WST INTEGER DEFAULT 0,
                _XAF INTEGER DEFAULT 0,
                _XAG INTEGER DEFAULT 0,
                _XAU INTEGER DEFAULT 0,
                _XCD INTEGER DEFAULT 0,
                _XOF INTEGER DEFAULT 0,
                _XPF INTEGER DEFAULT 0,
                _YER INTEGER DEFAULT 0,
                _ZAR INTEGER DEFAULT 0,
                _ZMW INTEGER DEFAULT 0,
                _ZWL INTEGER DEFAULT 0
            );
        """)
    
    con.close()
    print("Main DB is created.")

def AddID(chatID, chatType):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    cursor.execute("INSERT OR IGNORE INTO SettingsExchangeRates (chatID) values (?)",tuple([chatID]))
    cursor.execute("INSERT OR IGNORE INTO SettingsCryptoRates (chatID) values (?)",tuple([chatID]))
    if chatType=="group" or chatType=="supergroup":
        cursor.execute("INSERT OR IGNORE INTO SettingsGroups (chatID) values (?)",tuple([chatID]))
    else:
        cursor.execute("INSERT OR IGNORE INTO SettingsPrivateChats (chatID) values (?)",tuple([chatID]))
    con.commit()


def SetSetting(chatID, key, val, chatType):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    try:
        if chatType=="group" or chatType=="supergroup":
            cursor.execute("UPDATE OR ABORT SettingsGroups SET "+str(key)+"= "+str(val)+" WHERE chatID = "+str(chatID))
        else:
            cursor.execute("UPDATE OR ABORT SettingsPrivateChats SET "+str(key)+"= "+str(val)+" WHERE chatID = "+str(chatID))
        con.commit()
    except:
        print("No such column")

def SetCurrencySetting(chatID, currency, val):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE OR ABORT SettingsExchangeRates SET "+"_"+str(currency)+"= "+str(val)+" WHERE chatID = "+str(chatID))
        con.commit()
    except:
        print("No such column")

def SetCryptoSetting(chatID, crypto, val):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    try:
        cursor.execute("UPDATE OR ABORT SettingsCryptoRates SET "+str(crypto)+"= "+str(val)+" WHERE chatID = "+str(chatID))
        con.commit()
    except:
        print("No such column")

def GetAllSettings(chatID, chatType):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    con.row_factory = sql.Row
    cursor = con.cursor()
    try:
        if chatType=="group" or chatType=="supergroup":
            cursor.execute("SELECT * from SettingsGroups WHERE chatID = "+str(chatID))
            res = cursor.fetchone()
        else:
            cursor.execute("SELECT * from SettingsPrivateChats WHERE chatID = "+str(chatID))
            res = cursor.fetchone()
        return dict(res)
    except:
        print("No such chatID")
        return None

def GetSetting(chatID,key,chatType):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    try:
        if chatType=="group" or chatType=="supergroup":
            cursor.execute("SELECT "+str(key)+" from SettingsGroups WHERE chatID = "+str(chatID))
            res = cursor.fetchone()
        else:
            cursor.execute("SELECT "+str(key)+" from SettingsPrivateChats WHERE chatID = "+str(chatID))
            res = cursor.fetchone()
        return res[0]
    except:
        print("No such column")
        return None

def GetAllCurrencies(chatID):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    con.row_factory = sql.Row
    cursor = con.cursor()
    try:
        cursor.execute("SELECT * FROM SettingsExchangeRates WHERE chatID = "+str(chatID))
        res = dict(cursor.fetchone())
        return [k[1:] for k,v in res.items() if v==1]
    except:
        print("No such chatID")
        return None

def GetAllCrypto(chatID):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    con.row_factory = sql.Row
    cursor = con.cursor()
    try:
        cursor.execute("SELECT * FROM SettingsCryptoRates WHERE chatID = "+str(chatID))
        res = dict(cursor.fetchone())
        return [k for k,v in res.items() if v==1]
    except:
        print("No such chatID")
        return None

def ChatExists(chatID):
    chatID = int(chatID)
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM SettingsExchangeRates WHERE chatID = "+str(chatID)+")")
    res = cursor.fetchone()
    return res[0]

def IsBlacklisted(userID):
    userID = int(userID)
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM BlackList WHERE userID = "+str(userID)+")")
    res = cursor.fetchone()
    return res[0]

def ClearBlacklist(userID):
    userID = int(userID)
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    if userID==0:
        cursor.execute("DELETE FROM BlackList")
        con.commit()
        cursor.execute("VACUUM")
        con.commit()
        return 1
    else:
        try:
            cursor.execute("DELETE FROM BlackList WHERE userID = "+str(userID))
            con.commit()
            return 1
        except:
            print("No such userID")
            return None
 
def AddBlacklist(userID,chatID=0,chatName=""):
    chatID = int(chatID)
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    cursor.execute("INSERT OR IGNORE INTO BlackList (userID,chatID,chatName,banDate) values (?,?,?,DATETIME())",tuple([userID,chatID,chatName]))
    con.commit()

def GetBlacklist():
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * from BlackList")
    res = cursor.fetchall()
    return [k[0] for k in res]

def GetAdmins():
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * from AdminsList")
    res = cursor.fetchall()
    return [k[0] for k in res]

def IsAdmin(adminID):
    adminID = int(adminID)
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM AdminsList WHERE adminID = "+str(adminID)+")")
    res = cursor.fetchone()
    return res[0]

def AddAdmin(adminID):
    adminID = int(adminID)
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    cursor.execute("INSERT OR IGNORE INTO AdminsList (adminID) values ("+str(adminID)+")")
    con.commit()

def ClearAdmins(adminID):
    adminID = int(adminID)
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    if adminID==0:
        cursor.execute("DELETE FROM AdminsList")
        con.commit()
        return 1
    else:
        try:
            cursor.execute("DELETE FROM AdminsList WHERE adminID = "+str(adminID))
            con.commit()
            return 1
        except:
            print("No such adminID")
            return None

def GetListOfCurrencies():
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.execute("SELECT * FROM SettingsExchangeRates")
    names = [description[0] for description in cursor.description]
    names.pop(0)
    return [i[1:] for i in names]

def GetListOfCrypto():
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.execute("SELECT * FROM SettingsCryptoRates")
    names = [description[0] for description in cursor.description]
    names.pop(0)
    return [i[1:] for i in names]

def UpdateExchangeRatesDB(exchangeRates):
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    f = open("Dictionaries/currencies.json",encoding="utf-8")
    data = json.load(f)
    for cur, rate in exchangeRates.items():
        flag = next((item for item in data['currencies'] if item['code']==cur),None)
        try:
            cursor.execute("INSERT OR REPLACE INTO ExchangeRates (currency,flag,exchangeRates) values ('"+cur+"','"+flag["emoji"]+"',?)",tuple([rate]))
        except:
            continue
    con.commit()

def UpdateCryptoRatesDB(cryptoRates):
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    f = open("Dictionaries/currencies.json",encoding="utf-8")
    data = json.load(f)
    for cur, rate in cryptoRates.items():
        cursor.execute("INSERT OR REPLACE INTO CryptoRates (currency,flag,exchangeRates) values ('"+cur[:-4]+"','"+""+"',?)",tuple([rate]))
    con.commit()

def AddIDStats(chatID,chatType):
    con = sql.connect('DataBases/StatsData.sqlite')
    cursor = con.cursor()
    cursor.execute("INSERT OR IGNORE INTO ChatsUsage (chatID, chatType, timeAdded, lastTimeUse) values ("+str(chatID)+",'"+chatType+"',DATETIME(),DATETIME())")
    con.commit()

def UpdateChatUsage(chatID):
    con = sql.connect('DataBases/StatsData.sqlite')
    cursor = con.cursor()
    cursor.execute("UPDATE ChatsUsage SET lastTimeUse = DATETIME() WHERE chatID = "+str(chatID))
    con.commit()

def GetChatsAmount():
    con = sql.connect('DataBases/StatsData.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE chatType = 'private'")
    res = {}
    res['private']=cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE chatType = 'group' OR chatType = 'supergroup'")
    res['groups']=cursor.fetchone()[0]
    return res

def GetTimeStats():
    con = sql.connect('DataBases/StatsData.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE chatType = 'private'")
    res = {}
    res['private']=cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE chatType = 'group' OR chatType = 'supergroup'")
    res['groups']=cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE chatType = 'private' AND lastTimeUse > datetime('now', '-7 days')")
    res['activePrivateWeek'] = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE (chatType = 'group' OR chatType ='supergroup' ) AND lastTimeUse > datetime('now', '-7 days')")
    res['activeGroupsWeek'] = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE chatType = 'private' AND lastTimeUse > datetime('now', '-1 month')")
    res['activePrivateMonth'] = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE (chatType = 'group' OR chatType ='supergroup' ) AND lastTimeUse > datetime('now', '-1 month')")
    res['activeGroupsMonth'] = cursor.fetchone()[0]
    cursor.execute("INSERT INTO ChatsTimeStats (date,privateChatsAmount,groupChatsAmount,activeWeekPrivateChats,activeWeekGroupChats,activeMonthPrivateChats,activeMonthGroupChats) values (DATETIME(),?,?,?,?,?,?)",tuple(res.values()))
    con.commit()
    return res

def ProcessedCurrency(chatID, userID, processedCurrency, message, turnedOnCurrencies):
    values_q = [chatID, userID, processedCurrency, message]
    con = sql.connect('DataBases/StatsData.sqlite')
    cursor = con.cursor()
    query = "INSERT INTO ProcessedCurrencies (date, chatID, userID, proccesedCurrency ,message"
    for cur in turnedOnCurrencies:
        query = query +", _"+ cur
        values_q.append(1)
    query = query+") values (DATETIME(), ?,?,?,?"
    for cur in turnedOnCurrencies:
        query = query +",?"
    query = query+")"
    cursor.execute(query,tuple(values_q))
    con.commit()

def GetListOfFlags():
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ExchangeRates")
    res = cursor.fetchall()
    res_dict = {}
    for i in res:
        res_dict[i[0]]=i[1]
    return res_dict

def GetExchangeRates():
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ExchangeRates")
    res = cursor.fetchall()
    res_dict = {}
    for i in res:
        res_dict[i[0]]=i[2]
    return res_dict

def GetCryptoRates():
    con = sql.connect('DataBases/DataForBot.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM CryptoRates")
    res = cursor.fetchall()
    res_dict = {}
    for i in res:
        res_dict[i[0]]=i[2]
    return res_dict

def GetStatsInPeriod(days):
    con = sql.connect('DataBases/StatsData.sqlite')
    cursor = con.cursor()
    res = {}
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE chatType = 'private' AND lastTimeUse > datetime('now', '-"+str(days)+" days')")
    res['activePrivate'] = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM ChatsUsage WHERE (chatType = 'group' OR chatType ='supergroup' ) AND lastTimeUse > datetime('now', '-"+str(days)+" days')")
    res['activeGroups'] = cursor.fetchone()[0]
    return res

def AddReport(chatID, userID, message, reply=""):
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    cursor.execute("INSERT INTO Reports (date,chatID,userID,message,reply) values (DATETIME(),?,?,?,?)",tuple([chatID,userID,message,reply]))
    con.commit()

def ClearReports():
    con = sql.connect('DataBases/ServiceData.sqlite')
    cursor = con.cursor()
    cursor.execute("DELETE FROM Reports")
    con.commit()
    cursor.execute("VACUUM")
    con.commit()
