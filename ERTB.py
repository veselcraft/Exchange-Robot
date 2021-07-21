# Token
from Token import botToken

# Public libraries
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from numberize import numberizer
from threading import Thread
import sys
from datetime import datetime

# Own libraries
import DBH
from NewPrint import Print, EnableLogging, DisableLogging, PrintMainInfo
from SkipUpdates import EnableUpdates, DisableUpdates, IsUpdate
from GetExchangeRates import SheduleUpdate, SheduleCryptoUpdate 
from BlackList import IsUserInBlackList, LoadBlackList
import Processing
from Processing import AnswerText, LoadCurrencies, LoadCrypto, LoadDictionaries, LoadFlags, SearchValuesAndCurrencies, SpecialSplit, TextToDigit
import TextHelper as CustomMarkup
from TextHelper import LoadTexts, GetText

# Main variables
bot = Bot(token=botToken)
dp = Dispatcher(bot)

# Public commands
@dp.message_handler(commands=['about'])  # analog about and source
async def AboutMes(message: types.Message):
    if IsUserInBlackList(message.from_user.id):
        return
    IsChatExist(message.chat.id, message.chat.type)
    await message.reply(GetText(message.chat.id, "about", message.chat.type), reply_markup = CustomMarkup.DeleteMarkup(message.chat.id, message.chat.type))

@dp.message_handler(commands=['help'])
async def HelpMes(message: types.Message):
    if IsUserInBlackList(message.from_user.id):
        return
    IsChatExist(message.chat.id, message.chat.type)
    await message.reply(GetText(message.chat.id, "help", message.chat.type), reply_markup = CustomMarkup.DeleteMarkup(message.chat.id, message.chat.type))


@dp.message_handler(commands=['settings'])
async def SettingsMes(message: types.Message):
    pass


@dp.message_handler(commands=['donate'])
async def DonateMes(message: types.Message):
    if IsUserInBlackList(message.from_user.id):
        return
    IsChatExist(message.chat.id, message.chat.type)
    await message.reply(GetText(message.chat.id, "donate", message.chat.type), reply_markup = CustomMarkup.DonateMarkup(message.chat.id, message.chat.type))


@dp.message_handler(commands=['wrong'])
async def WrongMes(message: types.Message):
    pass

# Admin`s commands
@dp.message_handler(commands=['echo'])
async def EchoVoid(message: types.Message):
    await message.reply(message.text)


@dp.message_handler(commands=['numberofusers'])  # Analog of "count".
async def CountVoid(message: types.Message):
    pass

@dp.message_handler(commands=['newadmin']) 
async def AddAdminVoid(message: types.Message):
    if IsUserInBlackList(message.from_user.id):
        return
    if DBH.IsAdmin(message.from_user.id):
        newAdminID = message.text
        newAdminID = newAdminID.replace("/newadmin ", "")
        if newAdminID.isdigit():
            if not DBH.IsAdmin(newAdminID):
                DBH.AddAdmin(newAdminID)
                ListOfAdmins = DBH.GetAdmins()
                if newAdminID in ListOfAdmins:
                    message.reply("Новый администратор успешно добавлен.", CustomMarkup.GetText(message.chat.id, 'delete', message.chat.type))
                else:
                    message.reply("Не удалось добавить нового администратора.", CustomMarkup.GetText(message.chat.id, 'delete', message.chat.type))
            else:
                message.reply("Данный ID уже есть в списке администраторов.", CustomMarkup.GetText(message.chat.id, 'delete', message.chat.type))
        else:
            message.reply("В ID должны быть только цифры и минус.", CustomMarkup.GetText(message.chat.id, 'delete', message.chat.type))


@dp.message_handler(commands=['stats'])
async def StatsVoid(message: types.Message):
    pass


@dp.message_handler(commands=['pulloutalldata']) # analog "backup", "logs" and "reports".
async def BackupVoid(message: types.Message):
    pass

@dp.message_handler(commands=['unban'])
async def UnbanVoid(message: types.Message):
    if IsUserInBlackList(message.from_user.id):
        return
    if DBH.IsAdmin(message.from_user.id):
        unbanID = message.text
        unbanID = unbanID.replace("/unban ", "")
        if unbanID.isdigit():
            if DBH.IsBlacklisted(unbanID):
                DBH.ClearBlacklist(unbanID)
                if not DBH.IsBlacklisted(unbanID):
                    message.reply("Пользователь успешно разблокирован.", CustomMarkup.GetText(message.chat.id, 'delete', message.chat.type))
                else:
                    message.reply("Не удалось разблокировать пользователя.", CustomMarkup.GetText(message.chat.id, 'delete', message.chat.type))
            else:
                message.reply("Данный пользователь не находится в ЧС. Разблокировка не возможна.", CustomMarkup.GetText(message.chat.id, 'delete', message.chat.type))
        else:
            message.reply("В ID должны быть только цифры и минус.", CustomMarkup.GetText(message.chat.id, 'delete', message.chat.type))


# Technical commands
@dp.message_handler(commands=['start'])
async def StartVoid(message: types.Message):
    IsChatExist(message.chat.ID, message.chat.type)


@dp.message_handler(content_types=ContentType.ANY)
async def MainVoid(message: types.Message):
    def w2n(MesString):
        return numberizer.replace_numerals(MesString)

    # Checking if a user is on the blacklist
    if IsUserInBlackList(message.from_user.id):
        return

    # Get message text
    MessageText = message.text
    if message.photo or message.video is not None or message.document is not None:
        MessageText = message.caption
    if MessageText is None or MessageText == "":
        return

    # Logging basic information to terminal
    PrintMainInfo(message, MessageText)

    # Checking the chat in the database
    IsChatExist(message.chat.id, message.chat.type)

    # word to num
    OriginalMessageText = MessageText
    MessageText = MessageText.lower()
    MessageText = w2n(MessageText)
    Print(MessageText, "L")

    # Check digit
    if not any(map(str.isdigit, MessageText)):
        return

    # Preparing a message for searching currencies
    TextArray = SpecialSplit(MessageText)
    Print(str(TextArray), "L")

    # '5kk USD' to '5000000 USD'
    TextArray = TextToDigit(TextArray)
    Print(str(TextArray), "L")
    
    # Searching Currencies
    NumArray = SearchValuesAndCurrencies(TextArray)
    Print(str(NumArray), "L")

    # If there are no currencies, then work is interrupted
    if NumArray == [[],[],[],[]]:
        return

    result = AnswerText(NumArray, message.chat.id, message.chat.type)
    await message.reply(result, reply_markup = CustomMarkup.DeleteMarkup(message.chat.id, message.chat.type))
    for i in NumArray[1]:
        DBH.ProcessedCurrency(message.chat.id, message.from_user.id, Processing.ListOfCur[i], OriginalMessageText)
    for i in NumArray[3]:
        DBH.ProcessedCurrency(message.chat.id, message.from_user.id, Processing.ListOfCrypto[i], OriginalMessageText)

def CheckArgument(key: str, value: str) -> bool:
    isAllOkArg = True
    if key == "--logs" or key == "-l":
        if value == "on":
            EnableLogging()
        elif value == "off":
            DisableLogging()
        else:
            isAllOkArg = False
    elif key == "--admin" or key == "-a":
        if value.isdigit():
            if not DBH.IsAdmin(value):
                DBH.AddAdmin(value)
        else:
            isAllOkArg = False
    elif key == "--updates" or key == "-u":
        if value == "on":
            EnableUpdates()
        elif value == "off":
            DisableUpdates()
        else:
            isAllOkArg = False
    else:
        print("Error. Unknow argument '{}'".format(key))
    return isAllOkArg

def IsChatExist(chatID: str, chatType: str):
    if DBH.ChatExists(chatID):
        pass
    else:
        DBH.AddID(chatID, chatType)

def LoadDataForBot():
    DBH.DbIntegrityCheck()
    LoadBlackList()
    LoadCurrencies()
    LoadCrypto()
    LoadFlags()
    LoadDictionaries()
    LoadTexts()


if __name__ == '__main__':
    LoadDataForBot()

    if len(sys.argv) == 3:
        if not CheckArgument(sys.argv[1], sys.argv[2]):
            sys.exit()
    elif len(sys.argv) == 5 and sys.argv[1] != sys.argv[3]:
        if not CheckArgument(sys.argv[1], sys.argv[2]):
            sys.exit()
        elif not CheckArgument(sys.argv[3], sys.argv[4]):
            sys.exit()
    elif len(sys.argv) == 7 and sys.argv[1] != sys.argv[3] and sys.argv[1] != sys.argv[2] and sys.argv[2] != sys.argv[3]:
        if not CheckArgument(sys.argv[1], sys.argv[2]):
            sys.exit()
        elif not CheckArgument(sys.argv[3], sys.argv[4]):
            sys.exit()
        elif not CheckArgument(sys.argv[5], sys.argv[6]):
            sys.exit()
    elif len(sys.argv) == 5 and not sys.argv[1] != sys.argv[3] or len(sys.argv) == 7 and not (sys.argv[1] != sys.argv[3] and sys.argv[1] != sys.argv[2] and sys.argv[2] != sys.argv[3]):
        Print("Error. Duplicate argument.", "E")
        sys.exit()

    ThreadUpdateExchangeRates = Thread(target=SheduleUpdate)
    ThreadUpdateExchangeRates.start()
    ThreadUpdateCryptoRates = Thread(target=SheduleCryptoUpdate)
    ThreadUpdateCryptoRates.start()
    executor.start_polling(dp, skip_updates=IsUpdate())
