import DBH
import os
from NewPrint import Print

AllTexts = {}

def LoadTexts():
    global AllTexts
    UAtexts = {}
    RUtexts = {}
    ENtexts = {}
    try:
        listFiles = os.listdir("Texts")
        for i in listFiles:
            fileWithText = open("Texts/" + i)
            fileText = fileWithText.read()
            fileWithText.close()
            nameOfText = i[2:-4]
            if i.find("UA") == 0:
                UAtexts[nameOfText] = fileText
            elif i.find("EN") == 0:
                ENtexts[nameOfText] = fileText
            elif i.find("RU") == 0:
                RUtexts[nameOfText] = fileText
        AllTexts['ua'] = UAtexts
        AllTexts['ru'] = RUtexts
        AllTexts['en'] = ENtexts
    except:
        Print("Problem with Texts. Redownload, pls.", "E")

def GetText(chatID: str, nameOfText: str, chatType: str) -> str:
    lang = DBH.GetSetting(chatID, "lang", chatType)
    Print(lang, "E")
    dictLang = AllTexts[lang]
    return dictLang[nameOfText]