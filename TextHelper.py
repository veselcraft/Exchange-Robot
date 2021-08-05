from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

import DBH
import os
from NewPrint import Print

from Dictionaries.ButtonTexts import ButtonTexts
from Dictionaries.MessageTexts import MessageTexts

AllBigTexts = {}
ListOfNamesOfTextforBigTexts = []

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
        DonateMU.add(InlineKeyboardButton(dictLang['delete'], callback_data = "delete"))
    return DonateMU

def DeleteMarkup(chatID: str, chatType: str) -> InlineKeyboardMarkup:
    isDeleteButton = DBH.GetSetting(chatID, "deleteButton", chatType)
    DeleteMU = InlineKeyboardMarkup()
    if isDeleteButton:
        lang = DBH.GetSetting(chatID, "lang", chatType)
        dictLang = ButtonTexts[lang]
        DeleteMU.add(InlineKeyboardButton(dictLang['delete'], callback_data = "delete"))
    return DeleteMU

def SettingsMarkup(chatID: str, chatType: str) -> InlineKeyboardMarkup:
    lang = DBH.GetSetting(chatID, "lang", chatType)
    isDeleteButton = DBH.GetSetting(chatID, "deleteButton", chatType)
    dictLang = ButtonTexts[lang]
    SettingsMU = InlineKeyboardMarkup()
    SettingsMU.add(InlineKeyboardButton(dictLang['currencies'], callback_data = "cur"))
    SettingsMU.add(InlineKeyboardButton(dictLang['lang'], callback_data = "lang_menu"))
    SettingsMU.add(InlineKeyboardButton(dictLang['delete_button'], callback_data = "delbut_menu"))
    SettingsMU.add(InlineKeyboardButton(dictLang['flags'], callback_data = "flags"))
    if chatType != "private":
        SettingsMU.add(InlineKeyboardButton(dictLang['permisssions'], callback_data = "edit"))
    if isDeleteButton:
        SettingsMU.add(InlineKeyboardButton(dictLang['delete'], callback_data = "delete"))
    return SettingsMU

def DeleteButtonMenuMarkup(chatID: str, chatType: str) -> InlineKeyboardMarkup:
    def RulesMark(role: str, answDict) -> str:
        if answDict['deleteRules'] == role:
            return " ✅"
        else:
            return " ❌"
    
    lang = DBH.GetSetting(chatID, "lang", chatType)
    AllSettings = DBH.GetAllSettings(chatID, chatType)
    dictLang = ButtonTexts[lang]
    DeleteButtonMenuMU = InlineKeyboardMarkup()
    if AllSettings['deleteButton']:
        DeleteButtonMenuMU.add(InlineKeyboardButton(dictLang['delbutton'] + " ✅", callback_data = "delbut_button"))
        if chatType != "private":
            DeleteButtonMenuMU.add(InlineKeyboardButton(dictLang['creator'] + RulesMark('creator', AllSettings), callback_data = "delbut_creator"))
            DeleteButtonMenuMU.add(InlineKeyboardButton(dictLang['admins'] + RulesMark('admins', AllSettings), callback_data = "delbut_admins"))
            DeleteButtonMenuMU.add(InlineKeyboardButton(dictLang['everybody'] + RulesMark('everybody', AllSettings), callback_data = "delbut_everybody"))
    else:
        DeleteButtonMenuMU.add(InlineKeyboardButton(dictLang['delbutton'] + " ❌", callback_data = "delbut_button"))
    DeleteButtonMenuMU.add(InlineKeyboardButton(dictLang['back'], callback_data = "settings"))
    return DeleteButtonMenuMU

def LanguageMenuMarkup(chatID: str, chatType: str):
    def RulesMark(lang: str, answDict) -> str:
        if answDict['lang'] == lang:
            return " ✅"
        else:
            return " ❌"
    
    lang = DBH.GetSetting(chatID, "lang", chatType)
    AllSettings = DBH.GetAllSettings(chatID, chatType)
    dictLang = ButtonTexts[lang]
    LanguageMenuMU = InlineKeyboardMarkup()
    LanguageMenuMU.add(InlineKeyboardButton("🇬🇧EN" + RulesMark('en', AllSettings), callback_data = "lang_en"))
    LanguageMenuMU.add(InlineKeyboardButton("🇷🇺RU" + RulesMark('ru', AllSettings), callback_data = "lang_ru"))
    LanguageMenuMU.add(InlineKeyboardButton("🇺🇦UA" + RulesMark('ua', AllSettings), callback_data = "lang_ua"))
    LanguageMenuMU.add(InlineKeyboardButton(dictLang['back'], callback_data = "settings"))
    return LanguageMenuMU

def GetText(chatID: str, nameOfText: str, chatType: str) -> str:
    lang = DBH.GetSetting(chatID, "lang", chatType)
    answerText = ''
    if nameOfText in ListOfNamesOfTextforBigTexts:
        dictLang = AllBigTexts[lang]
        answerText = dictLang[nameOfText]
    elif nameOfText in ButtonTexts[lang]:
        dictLang = ButtonTexts[lang]
        answerText = dictLang[nameOfText]
    elif nameOfText in MessageTexts[lang]:
        dictLang = MessageTexts[lang]
        answerText = dictLang[nameOfText]
    return answerText