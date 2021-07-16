from aiogram.types.message import ContentType
consoleLog = True
import datetime

def Print(printingText):
    if consoleLog:
        print(printingText)

def EnableLogging():
    global consoleLog
    consoleLog = True

def DisableLogging():
    global consoleLog
    consoleLog = False

def PrintMainInfo(mes, mestxt):
    now = datetime.datetime.now()
    Print("")
    Print("******************************")
    Print(now.strftime("%d-%m-%Y %H:%M:%S"))
    Print("Username: " + str(mes.from_user.username) + " | User ID: " + str(mes.from_user.id) + " | First name: " + str(mes.from_user.first_name) + " | Last name: " + str(mes.from_user.last_name))
    Print("Chat ID: " + str(mes.chat.id) + " | Chat name: " + str(mes.chat.title) + " | Chat username: "+str(mes.chat.username) + " | Chat type: "+str(mes.chat.type))
    Print("")
    Print("Message: " + str(mestxt))