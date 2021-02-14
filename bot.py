#Token
from Token import botToken

#Public libraries
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from threading import Thread
import sys

#Own libraries
from DBH import DbIntegrityCheck
from NewPrint import Print, EnableLogging, DisableLogging
from SkipUpdates import EnableUpdates, DisableUpdates, IsUpdate
from GetExchangeRates import SheduleUpdate, UpdateExchangeRates

#Main variables
bot = Bot(token = botToken)
dp = Dispatcher(bot)

#Public commands
@dp.message_handler(commands=['about'])
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['help'])
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['settings'])
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['donate'])
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['wrong'])
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['source'])
async def main_void(message: types.Message):
    pass

#Admin`s commands
@dp.message_handler(commands=['echo'])
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['numberofusers']) #Analog of "count".
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['newadmin'])
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['stats'])
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['pulloutalldata']) #analog "backup", "logs" and "reports".
async def main_void(message: types.Message):
    pass

@dp.message_handler(commands=['unban'])
async def main_void(message: types.Message):
    pass

#Technical commands
@dp.message_handler(commands=['start'])
async def main_void(message: types.Message):
    pass

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
        print ("Error. Unknow argument '{}'".format(key))
    return isAllOkArg

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

    #ThreadUpdateExchangeRates = Thread(target=SheduleUpdate)
    #ThreadUpdateExchangeRates.start()
    DbIntegrityCheck()
    executor.start_polling(dp, skip_updates=IsUpdate())