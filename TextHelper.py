from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

import DBH
import os
from NewPrint import Print

AllBigTexts = {}
ListOfNamesOfTextforBigTexts = []
ButtonTexts = {'en': {'donate': 'Donate', 'delete': 'Delete'}, 'ru': {'donate': 'Поддержать', 'delete': "Удалить"}, 'ua': {'donate': 'Підтримати', 'delete': 'Видалити'}}

def LoadTexts():
    global AllBigTexts
    global ListOfNamesOfTextforBigTexts
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
            if nameOfText not in ListOfNamesOfTextforBigTexts:
                ListOfNamesOfTextforBigTexts.append(nameOfText)
            if i.find("UA") == 0:
                UAtexts[nameOfText] = fileText
            elif i.find("EN") == 0:
                ENtexts[nameOfText] = fileText
            elif i.find("RU") == 0:
                RUtexts[nameOfText] = fileText
        AllBigTexts['ua'] = UAtexts
        AllBigTexts['ru'] = RUtexts
        AllBigTexts['en'] = ENtexts
    except:
        Print("Problem with Texts. Redownload, pls.", "E")

def DonateMarkup(chatID: str, chatType: str) -> InlineKeyboardMarkup:
    lang = DBH.GetSetting(chatID, "lang", chatType)
    isDeleteButton = DBH.GetSetting(chatID, "deleteButton", chatType)
    dictLang = ButtonTexts[lang]
    DonateMU = InlineKeyboardMarkup()
    DonateMU.add(InlineKeyboardButton(dictLang['donate'], url="https://secure.wayforpay.com/payment/s3641f64becae", callback_data="donate"))
    if isDeleteButton:
        DonateMU.add(InlineKeyboardButton(dictLang['delete'], callback_data="delete"))
    return DonateMU

def DeleteMarkup(chatID: str, chatType: str) -> InlineKeyboardMarkup:
    isDeleteButton = DBH.GetSetting(chatID, "deleteButton", chatType)
    if isDeleteButton:
        lang = DBH.GetSetting(chatID, "lang", chatType)
        dictLang = ButtonTexts[lang]
        DeleteMU = InlineKeyboardMarkup()
        DeleteMU.add(InlineKeyboardButton(dictLang['delete'], callback_data="delete"))
    return DeleteMU

def GetText(chatID: str, nameOfText: str, chatType: str) -> str:
    lang = DBH.GetSetting(chatID, "lang", chatType)
    answerText = ''
    if nameOfText in ListOfNamesOfTextforBigTexts:
        dictLang = AllBigTexts[lang]
        answerText = dictLang[nameOfText]
    else:
        dictLang = ButtonTexts[lang]
        answerText = dictLang[nameOfText]
    return answerText