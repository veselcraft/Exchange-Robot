# Token
from Token import botToken

# Public libraries
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from threading import Thread
import sys

# Own libraries
import DBH
from NewPrint import Print, EnableLogging, DisableLogging, PrintMainInfo
from SkipUpdates import EnableUpdates, DisableUpdates, IsUpdate
from GetExchangeRates import SheduleUpdate, UpdateExchangeRates
from BlackList import IsUserInBlackList, LoadBlackList
from Processing import LoadCurrencies, LoadDictionaries, SearchValuesAndCurrencies, SpecialSplit, TextToDigit, GetCur

# Main variables
bot = Bot(token=botToken)
dp = Dispatcher(bot)

# Public commands


@dp.message_handler(commands=['about'])  # analog about and source
async def AboutMes(message: types.Message):
    pass


@dp.message_handler(commands=['help'])
async def HelpMes(message: types.Message):
    pass


@dp.message_handler(commands=['settings'])
async def SettingsMes(message: types.Message):
    pass


@dp.message_handler(commands=['donate'])
async def DonateMes(message: types.Message):
    pass


@dp.message_handler(commands=['wrong'])
async def WrongMes(message: types.Message):
    pass

# Admin`s commands


@dp.message_handler(commands=['echo'])
async def EchoVoid(message: types.Message):
    pass


@dp.message_handler(commands=['numberofusers'])  # Analog of "count".
async def CountVoid(message: types.Message):
    pass


@dp.message_handler(commands=['newadmin'])
async def AddAdminVoid(message: types.Message):
    pass


@dp.message_handler(commands=['stats'])
async def StatsVoid(message: types.Message):
    pass


# analog "backup", "logs" and "reports".
@dp.message_handler(commands=['pulloutalldata'])
async def BackupVoid(message: types.Message):
    pass


@dp.message_handler(commands=['unban'])
async def UnbanVoid(message: types.Message):
    pass

# Technical commands


@dp.message_handler(commands=['start'])
async def StartVoid(message: types.Message):
    pass


@dp.message_handler(content_types=ContentType.ANY)
async def MainVoid(message: types.Message):
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
    """ if DBH.ChatExists(message.chat.id):
        pass
    else:
        DBH.AddID(message.chat.id, message.chat.type) """

    # Check digit
    if not any(map(str.isdigit, MessageText)):
        return

    MessageText = MessageText.lower()
    TextArray = SpecialSplit(MessageText)
    Print(TextArray)


    # поиск валют, если их нет, то возврат обратно, если есть, то продолжить

    TextArray = TextToDigit(TextArray)
    Print(TextArray)

    NumArray = SearchValuesAndCurrencies(TextArray)
    Print(NumArray)

    textMes = ''
    for i in range(len(NumArray[0])):
        NumArray[1][i] = GetCur(NumArray[1][i])
        textMes += NumArray[0][i] + " " + NumArray[1][i] + "\n"


    await message.reply(textMes)


def CheckArgument(key, value):
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
            pass
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

def LoadDataForBot():
    DBH.DbIntegrityCheck()
    LoadBlackList()
    LoadCurrencies()
    LoadDictionaries()

if __name__ == '__main__':
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
        print("Error. Duplicate argument.")
        sys.exit()

    # ThreadUpdateExchangeRates = Thread(target=SheduleUpdate)
    # ThreadUpdateExchangeRates.start()
    LoadDataForBot()
    executor.start_polling(dp, skip_updates=IsUpdate())
